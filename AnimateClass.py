from sense_hat import SenseHat
import time
import threading

sense = SenseHat()
class Animate:
    def __init__(self, base, toggle="none"):
        self.base = base
        self.toggle = toggle
        # print(f"I was just created with base of {self.base}")

    def characterSelect(self, passedEvent):
        sense.clear()
        while True:
            sense.set_pixels(self.base)
            time.sleep(1)
            event = sense.stick.wait_for_event()
            if event.action == "pressed" and event.direction != passedEvent  and event.direction !="up" and event.direction != "middle":
                break
            if event.direction == "down":
                done = True
                return done 
            if event.direction == "middle":
                show_alert = True
                return show_alert

    # make async
    def longAnimate(self):
        count = 0
        while True:
            sense.set_pixels(self.base)
            time.sleep(1)
            print("it slept")
            sense.set_pixels(self.toggle)
            time.sleep(1) 
            print("it slept")
            count += 1
            print(count)
            # if thread stopped break the loop
            if count > 1:
                break

    def sadAnimate(self, toggle2, toggle3):
        count = 0 
        while True:
            sense.set_pixels(self.base)
            time.sleep(1)
            sense.set_pixels(self.toggle1)
            time.sleep(1) 
            sense.set_pixels(toggle2)
            time.sleep(1) 
            sense.set_pixels(toggle3)
            count += 1
            if count > 100:
                break