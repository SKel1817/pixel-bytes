from google.cloud import bigquery
from sense_hat import SenseHat
import DisplayClass
import requests
import os
import time
from datetime import datetime

# Set the path to your BigQuery key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/val/nielson-4160-f24-fc7ef783ed23.json"

# Initialize Sense HAT
sense = SenseHat()

# Default values
default_animal = "crab"
hungry = False
previous_animal = default_animal
previous_hungry = hungry

# BigQuery client
client = bigquery.Client()
dataset_id = "pixelbytes"  # Replace with your dataset ID
table_id = "user_data"      # Replace with your table ID

# Function to insert data into BigQuery
def insert_into_bigquery(date, temp, humidity, hunger_level, curr_avatar):
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)
    
    rows_to_insert = [{
        "Date": date,
        "Temp": temp,
        "Humidity": humidity,
        "Hunger_Level": hunger_level,
        "Curr_Avatar": curr_avatar
    }]
    
    errors = client.insert_rows_json(table, rows_to_insert)
    if errors:
        print(f"Failed to insert rows: {errors}")
    else:
        print("Inserted row successfully.")

def get_animal_data():
    url = 'http://104.197.69.67/save_avatar.php'
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        if data.get('status') == 'success':
            return data.get('animal', default_animal)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch animal data: {e}")
    return default_animal

def get_hunger():
    url = 'https://hunger-tracker-770213444308.us-central1.run.app/manage_hunger'
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get('status') == 'hungry'
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch hunger status: {e}")
    return False

def get_hunger_level():
    url = 'https://hunger-tracker-770213444308.us-central1.run.app/manage_hunger'
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        return int(data.get('hunger_level', 0))
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch hunger level: {e}")
    return 0

# Main program loop
print("Welcome to this program. God, I hope it works better now.")
last_insert_time = time.time()

while True:
    temp = int(sense.get_temperature())
    humidity = int(sense.get_humidity())
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    print(f"Date: {current_date}, Temp: {temp}, Humidity: {humidity}")
    print(f"Default animal: {default_animal}, Hungry: {hungry}")
    
    animal = DisplayClass.Display(default_animal)
    if hungry:
        animal.sadScreen()
    else:
        animal.defaultScreen()

    new_animal = get_animal_data()
    new_hungry = get_hunger()
    hunger_level = get_hunger_level()

    # Insert into BigQuery every 2 hours or upon change
    if (time.time() - last_insert_time > 7200 or 
        new_animal != previous_animal or 
        new_hungry != previous_hungry):
        
        print(f"Inserting into BigQuery: {current_date}, {temp}, {humidity}, {hunger_level}, {new_animal}")
        insert_into_bigquery(current_date, temp, humidity, hunger_level, new_animal)
        
        last_insert_time = time.time()
        previous_animal = new_animal
        previous_hungry = new_hungry

    # Update current states
    default_animal = new_animal
    hungry = new_hungry
    
    time.sleep(2)  # Adjust as needed
