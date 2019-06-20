cars = ["audi", "bmw", "ford", "honda"]
for i in cars:
    if i == "bmw":
        print("BMW")
    else:
        print(i.title())

# user input
# myVal = input("Enter a value: ")
# print(myVal)

aVal = 20
if aVal < 50 and aVal > 10:
    print("val is 20")

toppings = ["cheese", "pepperoni", "anchovies"]
if "cheese" in toppings:
    print("topping is in pizza")

kidAge = 17
if kidAge < 4:
    print("kids are free")
elif kidAge < 18:
    print("teenager price is $20")
else:
    print("adult price is $30")

# using two lists with if statements
