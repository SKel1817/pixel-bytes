import requests
import time
import DisplayClass
default_animal = "crab"
def get_animal_data():
    # Replace with the actual URL of your save_avatar.php endpoint
    url = 'http://104.197.69.67/save_avatar.php'  # Replace <vm-ip> with your VM's IP or domain
    max_attempts = 1
    attempt = 0

    while attempt < max_attempts:
        try:
            print("here")
            # Make a GET request to retrieve the currently selected avatar
            response = requests.get(url, timeout=5)  # Timeout set to 10 seconds for each attempt
            response.raise_for_status()  # Check if the request was successful

            # Parse the JSON response
            data = response.json()

            # Extract the animal or handle the error message
            if data.get('status') == 'success':
                animal = data.get('animal', default_animal)
                print(f'The animal to display is: {animal}')
                return animal
            else:
                print(f'Error: {data.get("message", "Unknown error")}')
                return default_animal

        except requests.exceptions.RequestException as e:
            attempt += 1
            print(f'Attempt {attempt} failed: {e}')

            # Wait before the next attempt (e.g., 10 seconds)
            time.sleep(1)

    # If all attempts fail, return the default animal
    print(f'All {max_attempts} attempts failed. Returning default animal: {default_animal}')
    return default_animal


print("Welcome to this program god I hope it works better now")
while True:
    animal = DisplayClass.Display(default_animal)
    animal.defaultScreen()
    get_animal_data()