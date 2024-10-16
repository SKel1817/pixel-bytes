# from AnimalClass import Animal as ab
import DisplayClass
from sense_hat import SenseHat
import threading


print("Welcome to this program god I hope it works better now")
default_animal = "crab"
# def event_has_happened(callback):
#     sense = SenseHat()
#     while True:
#         event = sense.stick.wait_for_event()  # Blocking call
#         direction = event.direction
#         callback(direction)
# def handle_direction(direction):
#     global default_animal
#     if direction == "up":

#         new_animal = animal.menuScreen()
#         print(new_animal)
#         default_animal = new_animal
#         return direction
while True:
    animal = DisplayClass.Display(default_animal)
    animal.defaultScreen()
    print("made it here")
    sense = SenseHat()
    event = event = sense.stick.wait_for_event()
    if event.direction  == "middle":
        print("print here!")
        new_animal = animal.menuScreen()
        print(new_animal)
        default_animal = new_animal
