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
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.odometer = 0

    def setOdometer(self, miles):
        self.odometer = miles

    def getMiles(self):
        return self.odometer

    def carType(self):
        message = f"{self.brand}, {self.model}, {self.odometer} miles"
        return message

myCar = Car('vw', 'jetta')
print(myCar.carType())
myCar.setOdometer(55)
pri





