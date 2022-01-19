class Thermometer():
    def __init__(self, t):
        self.temperature = t
        
    def show_status(self):
        if self.temperature > 41.0:
            print(f"{self.temperature} - CRITICAL TEMPERATURE!")
        elif self.temperature > 37.0:
            print(f"{self.temperature} - fever")
        else:
            print(f"{self.temperature}")
        

import random

x = random.randint(340,420)
t=x/10
t = Thermometer(t)
t.show_status()