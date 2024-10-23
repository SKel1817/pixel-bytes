# from AnimalClass import Animal as ab
import DisplayClass
import requests
default_animal = "crab"
def get_animal_data():
    try:
        print("here")
        response = requests.get('http://104.197.69.67/save_avatar.php')
        print("got past this bit")
        response.raise_for_status()
        print("okay?")
        data = response.json()
        print("we shoudl be fine")
        animal = data.get('animal', 'default animal')
        print(f'The animal to display is: {animal}')
        print("what the hell")
        default_animal = animal
        # Add logic to display the animal on the Pi
        return default_animal
    except requests.exceptions.RequestException as e:
        print(f'Error fetching animal data: {e}')

print("Welcome to this program god I hope it works better now")
while True:
    animal = DisplayClass.Display(default_animal)
    animal.defaultScreen()
    get_animal_data()