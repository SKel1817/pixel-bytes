# from AnimalClass import Animal as ab
import DisplayClass
import requests
def get_animal_data():
    try:
        response = requests.get('http://104.197.69.67/save_avatar.php')
        response.raise_for_status()
        data = response.json()
        animal = data.get('animal', 'default animal')
        print(f'The animal to display is: {animal}')
        default_animal = animal
        # Add logic to display the animal on the Pi
    except requests.exceptions.RequestException as e:
        print(f'Error fetching animal data: {e}')

if __name__ == "__main__":
    get_animal_data()

print("Welcome to this program god I hope it works better now")
default_animal = "crab"
while True:
    animal = DisplayClass.Display(default_animal)
    animal.defaultScreen()
    get_animal_data()




