import requests

def get_animal_data():
    # Replace with the actual URL of your save_avatar.php endpoint
    url = 'http://104.197.69.67/save_avatar.php'  # Replace <vm-ip> with your VM's IP or domain

    try:
        # Make a GET request to retrieve the currently selected avatar
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the JSON response
        data = response.json()

        # Extract the animal or handle the error message
        if data.get('status') == 'success':
            animal = data.get('animal', 'default animal')
            print(f'The animal to display is: {animal}')
        else:
            print(f'Error: {data.get("message", "Unknown error")}')

    except requests.exceptions.RequestException as e:
        print(f'Error fetching animal data: {e}')

if __name__ == "__main__":
    get_animal_data()
