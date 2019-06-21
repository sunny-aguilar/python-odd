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

# car class
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


class ElectricCar(Car):
    """ electric version of car class """
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = 75



my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.descriptive_name())


