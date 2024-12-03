# Import the Vehicle class to create a Car class that inherits from it
from vehicle import Vehicle

class Car(Vehicle):
    # Override the go() method to return a custom string for the Car class
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    pass