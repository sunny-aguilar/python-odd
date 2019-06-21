# classes
class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"Restarant name: {self.name}")
        print(f"Cuisine type: {self.type}")

    def open_restaurant(self):
        print(f"{self.name} is open for business")


my_restaurant = Restaurant("Pizza Hut", "Pizza")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# dog class
class Dog:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def bark(self):
        print("Bark bark bark!")

    def roll_over(self):
        print(f"{self.name} is rolling over")


