""" classes to represent an electric car """


# battery class
class Battery():
    def __init__(self):
        self.battery = 75

    def describe_battery(self):
        """ print a statement describing battery """
        print(f"This car has a {self.battery}-kWh battery.")


# child class has a battery class
class ElectricCar(Car):
    """ electric version of car class """
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_tank(self):
        print("Electric cars don't have gas tanks!")