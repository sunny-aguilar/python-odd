""" car super class """

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def setOdometer(self, miles):
        if miles > self.odometer:
            self.odometer = miles
        else:
            print("error setting mileage")

    def getMiles(self):
        return self.odometer

    def carType(self):
        message = f"{self.make}, {self.model}, {self.odometer} miles"
        return message

    def descriptive_name(self):
        name = f"{self.make} {self.model}"
        return name.title()

    def fill_tank(self):
        print("Filling gas tank")


