from sense_hat import SenseHat
import time
import threading
import AnimateClass as ac

sense = SenseHat()
class Display:
    def __init__(self, animal="frog", hunger=5):
        self.animal = animal
        self.hunger = hunger

    def menuScreen(self):
        # find better way to do this cause this is ugly as hell
        # animal = self.animal
        new_animal = ""
        crab = self.animalIndex("crabBase")
        frog = self.animalIndex("frogBase")
        cat = self.animalIndex("catBase")
        dog = self.animalIndex("dogBase")
        alert = self.animalIndex("alertScreen")
        show_frog = False
        show_crab = False
        show_cat = False
        show_dog =  False
        shown_count = 0
        while True:
            event = sense.stick.wait_for_event()  # Blocking call
            direction = event.direction
            print(direction)
            print(event.action)
            done = False
            show_alert = False
            # use the joystick to change what animal is on the screen 
            # left for frog
            if ((direction == "left" or direction == "right") and show_frog == False):
                Animal = ac.Animate(frog)
                Animal.characterSelect("left" )
                show_frog = True
                shown_count += 1
                new_animal = "frog"
                continue
            # right for crab
            if ((direction == "left" or direction == "right") and show_crab == False):
                Animal = ac.Animate(crab)
                Animal.characterSelect(direction)
                show_crab = True
                shown_count += 1
                new_animal = "crab"
                continue
            if ((direction == "left" or direction == "right") and show_cat == False):
                Animal = ac.Animate(cat)
                Animal.characterSelect(direction)
                show_cat = True
                shown_count += 1
                new_animal = "cat"
                continue
            if ((direction == "left" or direction == "right") and show_dog == False):
                Animal = ac.Animate(dog)
                Animal.characterSelect(direction)
                show_dog = True
                shown_count += 1
                new_animal= "dog"
                continue
            if done == "true" or direction == "down":
                return new_animal
            if shown_count == 4 and done == False:
                shown_count = 0
                show_frog = False
                show_crab = False
                show_cat = False
                show_dog =  False
            #press the button 
            if direction == "middle" or show_alert == True:
                Animal = ac.Animate(alert, alert)
                Animal.characterSelect("middle")
                if direction == "up":
                    # reset the timer
                    print("timer reset!")
                    
    def defaultScreen(self):
        # check for weather and display proper long animation for each weather type
        temp = sense.temperature
        humidity = sense.humidity
        weather_happening = False
        if (temp > 20 and humidity < 80):
            weather_happening = True
            weather = "Sun"   
        if (temp < 20 and humidity > 80):
            weather_happening = True
            weather = "Rain"
        if (temp < 0):
            weather_happening = True
            weather = "Snow"
        if weather_happening == False:
            print("no weather")
            weather = ""
        baseName = self.animalIndex(self.animal + weather + "Base")
        toggleName = self.animalIndex(self.animal + weather + "Toggle")
        animation = ac.Animate(baseName, toggleName)
        animation.longAnimate()
        print("hello???")
        if self.hunger == 0:
            print("sad")
            baseName = self.animalIndex(self.animal + "SadBase")
            toggleName1 = self.animalIndex(self.animal + "SadToggle1")
            toggleName2 = self.animalIndex(self.animal + "SadToggle2")
            toggleName3 = self.animalIndex(self.animal + "SadToggle3")
            print(baseName)
            print(toggleName1)
            print(toggleName2)
            print(toggleName3)
            animation = ac.Animate(baseName, toggleName1)
            animation.sadAnimate(toggleName2, toggleName3)
    def animalIndex(self, name):
        r = (255, 0, 0)  # Red
        o = (225, 125, 0) # Orange
        d = (255, 110, 5) # Dark Orange
        t = (160, 82,45) # Tan
        i = (150, 90, 60) # Light Brown
        m = (130, 69, 10) # Mid Brown
        a = (110, 65, 30) # Dark Brown
        l = (255, 200, 0) # Gold
        y = (225, 225, 0) # Yellow
        g = (0, 255, 0) # Green
        e = (15, 130, 169) # Teal
        h = (250, 220, 235) # Light Blue
        b = (0, 0, 255) # Blue
        p = (200, 50, 200) # Purple
        c = (0, 0, 0) # Black
        z = (70, 70, 70) # Grey
        w = (255, 255, 255) # White
        

        index = {
            "alertScreen" : [
                c, c, c, c, c, c, c, c,
                c, y, c, c, c, c, c, c,
                c, y, c, c, c, t, t, c, 
                c, y, c, c, c, t, t, c,
                c, c, c, c, w, c, c, c,
                c, y, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c
            ],

            "crabBase" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, r, z, c, c, z, r, c,
                r, r, c, r, r, c, r, r,
                c, c, r, r, r, r, c, c,
                c, c, r, r, r, r, c, c,
                c, r, c, c, c, c, r, c
            ],

            "crabToggle" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                r, r, z, c, c, z, r, r,
                r, r, c, r, r, c, r, r,
                c, c, r, r, r, r, c, c,
                c, c, r, r, r, r, c, c,
                c, r, c, c, c, c, r, c
            ],

            "crabSadBase" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, r, z, c, c, z, r, c,
                r, r, c, r, r, b, r, r,
                c, c, r, r, r, r, c, c,
                c, c, r, r, r, r, c, c,
                c, r, c, c, c, c, r, c
            ],

            "crabSadToggle1" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, r, z, c, c, z, r, c,
                r, r, c, r, r, c, r, r,
                c, c, r, r, r, b, c, c,
                c, c, r, r, r, r, c, c,
                c, r, c, c, c, c, r, c
            ],

            "crabSadToggle2" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, r, z, c, c, z, r, c,
                r, r, c, r, r, c, r, r,
                c, c, r, r, r, r, c, c,
                c, c, r, r, r, b, c, c,
                c, r, c, c, c, c, r, c
            ],

            "crabSadToggle3" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, r, z, c, c, z, r, c,
                r, r, c, r, r, c, r, r,
                c, c, r, r, r, r, c, c,
                c, c, r, r, r, r, c, c,
                c, r, c, c, c, b, r, c
            ],

            "crabSunBase" : [
                c, c, c, c, c, y, l, o,
                c, c, c, c, c, c, y, l,
                c, c, c, c, c, c, c, y,
                c, r, z, c, c, z, r, c,
                r, r, c, r, r, c, r, r,
                c, c, r, r, r, r, c, c,
                c, c, r, r, r, r, c, c,
                c, r, c, c, c, c, r, c
            ],

            "crabSunToggle" : [
                c, c, c, c, c, y, l, o,
                c, c, c, c, c, c, y, l,
                c, c, c, c, c, c, c, y,
                r, r, z, c, c, z, r, r,
                r, r, c, r, r, c, r, r,
                c, c, r, r, r, r, c, c,
                c, c, r, r, r, r, c, c,
                c, r, c, c, c, c, r, c
            ],

            "crabRainBase" : [
                c, b, c, c, c, c, c, b,
                c, c, c, c, b, c, c, c,
                c, c, b, c, c, c, c, c,
                c, c, c, c, c, c, b, c,
                b, c, z, c, c, z, c, c,
                c, c, r, r, r, r, c, c,
                c, r, r, r, r, r, r, c,
                c, r, r, r, r, r, r, c
            ],

            "crabRainToggle" : [
                c, c, c, c, c, c, c, c,
                c, b, c, c, c, c, c, b,
                c, c, c, c, b, c, c, c,
                c, c, b, c, c, c, c, c,
                c, c, z, c, c, z, b, c,
                b, c, r, r, r, r, c, c,
                c, r, r, r, r, r, r, c,
                c, r, r, r, r, r, r, c
            ],

            "crabSnowBase" : [
                c, h, c, c, c, c, c, h,
                c, c, c, c, h, c, c, c,
                c, c, h, c, c, c, c, c,
                c, c, c, c, c, c, c, h,
                h, z, c, c, c, z, c, c,
                c, c, p, p, p, c, c, c,
                c, p, p, p, p, p, c, c,
                c, p, p, p, p, p, c, c
            ],

            "crabSnowToggle" : [
                c, c, c, c, c, c, c, c,
                c, h, c, c, c, c, c, h,
                c, c, c, c, h, c, c, c,
                c, c, h, c, c, c, c, c,
                c, c, z, c, c, c, z, h,
                h, c, c, p, p, p, c, c,
                c, c, p, p, p, p, p, c,
                c, c, p, p, p, p, p, c
            ],

            "frogBase" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, z, c, c, z, c, c,
                c, c, c, g, g, c, c, c,
                c, c, g, g, g, g, c, c,
                c, c, g, g, g, g, c, c,
                c, g, g, c, c, g, g, c
            ],

            "frogToggle" : [
                c, c, z, c, c, z, c, c,
                c, c, c, g, g, c, c, c,
                c, c, g, g, g, g, c, c,
                c, c, g, g, g, g, c, c,
                c, c, g, c, c, g, c, c,
                c, c, g, c, c, g, c, c,
                c, g, g, c, c, g, g, c,
                c, c, c, c, c, c, c, c
            ],

            "frogSadBase" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, z, c, c, z, c, c,
                c, c, c, g, g, b, c, c,
                c, c, g, g, g, g, c, c,
                c, c, g, g, g, g, c, c,
                c, g, g, c, c, g, g, c
            ],

            "frogSadToggle1" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, z, c, c, z, c, c,
                c, c, c, g, g, c, c, c,
                c, c, g, g, g, b, c, c,
                c, c, g, g, g, g, c, c,
                c, g, g, c, c, g, g, c
            ],

            "frogSadToggle2" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, z, c, c, z, c, c,
                c, c, c, g, g, c, c, c,
                c, c, g, g, g, g, c, c,
                c, c, g, g, g, b, c, c,
                c, g, g, c, c, g, g, c

            ],

            "frogSadToggle3" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, z, c, c, z, c, c,
                c, c, c, g, g, c, c, c,
                c, c, g, g, g, g, c, c,
                c, c, g, g, g, g, c, c,
                c, g, g, c, c, b, g, c
            ],

            "frogSunBase" : [
                c, c, c, c, c, y, l, o,
                c, c, c, c, c, c, y, l,
                c, c, c, c, c, c, c, y,
                c, c, z, c, c, z, c, c,
                c, c, c, g, g, c, c, c,
                c, c, g, g, g, g, c, c,
                c, c, g, g, g, g, c, c,
                c, g, g, c, c, g, g, c
            ],

            "frogSunToggle" : [
                c, c, z, c, c, z, l, o,
                c, c, c, g, g, c, y, l,
                c, c, g, g, g, g, c, y,
                c, c, g, g, g, g, c, c,
                c, c, g, c, c, g, c, c,
                c, c, g, c, c, g, c, c,
                c, g, g, c, c, g, g, c,
                c, c, c, c, c, c, c, c
            ],

            "frogRainBase" : [
                b, c, c, c, c, c, c, c,
                c, c, c, c, b, c, c, c,
                c, c, c, c, c, c, c, c,
                c, b, z, c, c, z, c, c,
                c, c, c, g, g, c, c, b,
                c, c, g, g, g, g, c, c,
                c, c, g, g, g, g, c, c,
                c, g, g, c, c, g, g, c
            ],

            "frogRainToggle" : [
                c, c, c, c, c, c, b, c,
                b, c, c, c, c, c, c, c,
                c, c, c, c, b, c, c, c,
                c, c, z, c, c, z, c, c,
                c, b, c, g, g, c, c, c,
                c, c, g, g, g, g, c, b,
                c, c, g, g, g, g, c, c,
                c, g, g, c, c, g, g, c
            ],

            "frogSnowBase" : [
                h, c, c, c, c, c, c, c,
                c, c, c, c, h, c, c, c,
                c, c, c, c, c, c, c, c,
                c, h, c, c, c, c, c, c,
                c, c, z, c, c, z, c, h,
                c, c, c, e, e, c, c, c,
                c, c, e, e, e, e, c, c,
                c, c, e, e, e, e, c, c
            ],

            "frogSnowToggle" : [
                c, c, c, c, c, c, h, c,
                h, c, c, c, c, c, c, c,
                c, c, c, c, h, c, c, c,
                c, c, c, c, c, c, c, c,
                c, h, z, c, c, z, c, c,
                c, c, c, e, e, c, c, h,
                c, c, e, e, e, e, c, c,
                c, c, e, e, e, e, c, c
            ], 

            "catBase" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                o, c, c, c, o, c, o, c,
                o, o, c, c, z, o, z, c,
                c, o, o, o, o, o, o, c,
                c, o, o, o, o, o, c, c,
                c, o, o, c, o, o, c, c
            ],

            "catToggle" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, o, c, c, c, c, c,
                c, o, o, c, o, c, o, c,
                c, o, c, c, z, o, z, c,
                c, o, o, o, o, o, o, c,
                c, o, o, o, o, o, c, c,
                c, o, o, c, o, o, c, c
            ],

            "catSadBase" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, o, c, o, c,
                c, c, c, c, z, o, z, c,
                d, o, o, o, o, o, b, c,
                d, d, o, o, o, o, c, c,
                c, o, d, c, o, o, c, c
            ],

            "catSadToggle1" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, o, c, o, c,
                c, c, c, c, z, o, z, c,
                d, o, o, o, o, o, o, c,
                d, d, o, o, o, o, b, c,
                c, o, d, c, o, o, c, c
            ],

            "catSadToggle2" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, o, c, o, c,
                c, c, c, c, z, o, z, c,
                d, o, o, o, o, o, o, c,
                d, d, o, o, o, o, c, c,
                c, o, d, c, o, o, b, c
            ],

            "catSadToggle3" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, c, o, c, o, c,
                c, c, c, c, z, o, z, c,
                d, o, o, o, o, o, o, c,
                d, d, o, o, o, o, c, c,
                c, o, d, c, o, o, c, c
            ],

            "catSunBase" : [
                c, c, c, c, c, y, l, o,
                c, c, c, c, c, c, y, l,
                c, c, c, c, c, c, c, y,
                o, c, c, c, o, c, o, c,
                o, o, c, c, z, o, z, c,
                c, o, o, o, o, o, o, c,
                c, o, o, o, o, o, c, c,
                c, o, o, c, o, o, c, c
            ],

            "catSunToggle" : [
                c, c, c, c, c, y, l, o,
                c, c, c, c, c, c, y, l,
                c, c, c, c, c, c, c, y,
                c, o, o, c, o, c, o, c,
                c, o, c, c, z, o, z, c,
                c, o, o, o, o, o, o, c,
                c, o, o, o, o, o, c, c,
                c, o, o, c, o, o, c, c
            ],

            "catRainBase" : [
                c, c, c, c, c, c, b, c,
                c, c, b, c, c, c, c, c,
                c, c, c, c, b, c, c, c,
                b, c, c, c, c, o, c, o,
                c, c, c, c, c, o, o, o,
                c, c, o, o, o, z, o, z,
                c, d, o, o, o, o, o, o,
                c, d, d, d, o, o, o, c
            ],

            "catRainToggle" : [
                c, b, c, c, c, c, c, c,
                c, c, c, c, c, c, b, c,
                c, c, b, c, c, c, c, c,
                c, c, c, c, b, o, c, o,
                b, c, c, c, c, o, o, o,
                c, c, o, o, o, z, o, z,
                c, d, o, o, o, o, o, o,
                c, d, d, d, o, o, o, c
            ],

            "catSnowBase" : [
                c, c, c, c, c, c, h, c,
                c, c, h, c, c, c, c, c,
                c, c, c, c, h, c, c, c,
                h, c, c, c, c, c, c, c,
                c, c, c, c, c, o, c, o,
                c, c, o, o, o, o, o, o,
                c, d, o, o, o, z, o, z,
                c, d, d, d, o, o, o, o
            ],

            "catSnowToggle" : [
                c, c, c, h, c, c, c, c,
                c, c, c, c, c, c, h, c,
                c, c, h, c, c, c, c, c,
                c, c, c, c, h, c, c, c,
                h, c, c, c, c, o, c, o,
                c, c, o, o, o, o, o, o,
                c, d, o, o, o, z, o, z,
                c, d, d, d, o, o, o, o
            ],

            "dogBase" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, a, a, c, a, a,
                i, c, c, a, m, m, m, a,
                i, i, c, a, z, m, z, a,
                c, m, m, m, m, m, m, c,
                c, m, m, m, m, m, c, c,
                c, m, m, c, m, m, c, c
            ],

            "dogToggle" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, i, a, a, c, a, a,
                c, i, i, a, m, m, m, a,
                c, i, c, a, z, m, z, a,
                c, m, m, m, m, m, m, c,
                c, m, m, m, m, m, c, c,
                c, m, m, c, m, m, c, c
            ],

            "dogSadBase" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, a, a, c, a, a,
                c, c, c, a, m, m, m, a,
                c, c, c, a, z, m, z, a,
                i, m, m, m, m, m, b, c,
                i, i, m, m, m, m, c, c,
                c, m, m, c, m, m, c, c
            ],

            "dogSadToggle1" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, a, a, c, a, a,
                c, c, c, a, m, m, m, a,
                c, c, c, a, z, m, z, a,
                i, m, m, m, m, m, m, c,
                i, i, m, m, m, m, b, c,
                c, m, m, c, m, m, c, c
            ],

            "dogSadToggle2" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, a, a, c, a, a,
                c, c, c, a, m, m, m, a,
                c, c, c, a, z, m, z, a,
                i, m, m, m, m, m, m, c,
                i, i, m, m, m, m, c, c,
                c, m, m, c, m, m, b, c
            ],

            "dogSadToggle3" : [
                c, c, c, c, c, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, c, a, a, c, a, a,
                c, c, c, a, m, m, m, a,
                c, c, c, a, z, m, z, a,
                i, m, m, m, m, m, m, c,
                i, i, m, m, m, m, c, c,
                c, m, m, c, m, m, c, c
            ],

            "dogSunBase" : [
                o, l, y, c, c, c, c, c,
                l, y, c, c, c, c, c, c,
                y, c, c, a, a, c, a, a,
                i, c, c, a, m, m, m, a,
                i, i, c, a, z, m, z, a,
                c, m, m, m, m, m, m, c,
                c, m, m, m, m, m, c, c,
                c, m, m, c, m, m, c, c
            ],

            "dogSunToggle" : [
                o, l, y, c, c, c, c, c,
                l, y, c, c, c, c, c, c,
                y, c, i, a, a, c, a, a,
                c, i, i, a, m, m, m, a,
                c, i, c, a, z, m, z, a,
                c, m, m, m, m, m, m, c,
                c, m, m, m, m, m, c, c,
                c, m, m, c, m, m, c, c
            ],

            "dogRainBase" : [
                c, c, c, c, b, c, c, c,
                c, c, c, c, c, c, b, c,
                c, c, b, c, a, a, c, a,
                c, c, c, c, a, m, m, m,
                b, c, c, c, a, z, m, z,
                c, i, m, m, m, m, m, m,
                i, m, m, m, m, m, m, c,
                i, i, m, m, m, m, m, m
            ],

            "dogRainToggle" : [
                c, b, c, c, c, c, c, c,
                c, c, c, c, b, c, c, c,
                c, c, c, c, a, a, b, a,
                c, c, b, c, a, m, m, m,
                c, c, c, c, a, z, m, z,
                b, i, m, m, m, m, m, m,
                i, m, m, m, m, m, m, c,
                i, i, m, m, m, m, m, m
            ],

            "dogSnowBase" : [
                h, c, c, c, c, c, c, c,
                c, c, c, c, h, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, h, c, c, c, c, h,
                c, c, c, c, c, c, c, c,
                c, c, i, a, a, m, a, a,
                c, i, m, a, m, m, m, a,
                c, i, i, m, m, m, m, c
            ],

            "dogSnowToggle" : [
                c, c, c, c, c, c, h, c,
                h, c, c, c, c, c, c, c,
                c, c, c, c, h, c, c, c,
                c, c, c, c, c, c, c, c,
                c, c, h, c, c, c, c, h,
                c, i, a, a, m, a, a, c,
                i, m, a, m, m, m, a, c,
                i, i, m, m, m, m, c, c
            ]
        }
        return index[name]