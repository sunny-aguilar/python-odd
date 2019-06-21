# classes
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"Restarant name: {self.name}")
        print(f"Cuisine type: {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is open for business")


my_restaurant = Restaurant("Pizza Hut", "Pizza")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print('\n')

# dog class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Bark bark bark!")

    def roll_over(self):
        print(f"{self.name} is rolling over")


my_dog = Dog("Moemoe", "Terrier")
my_dog.bark()
my_dog.roll_over()
print('\n')


""" import car class """
from car import Car, ElectricCar, Battery


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_tank()

