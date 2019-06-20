first = "sandro"
last = "aguilar"
myString = f"hello, {first} {last}"

print(myString.title())

paddedWord = "strip right   "
print(paddedWord.rstrip())

# sort a list
cars = ["toyota", "chevy", "bmw", "ford", "audit"]
cars.sort()
print(cars)

# reverse a list
cars.reverse()
print(cars)

# list length
print(len(cars))

# vacation spots
locations = ["egypt", "greece", "cancun", "japan", "china"]
print(locations)
print(sorted(locations))
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
print("\n")

# out of bounds access
access = [1, 2, 3, 4, 5]
print(access[4])
print("\n")

# looping through a list
for i in access:
    print(i)
print("\n")

actors = ["brad", "keanu", "ripley"]
for actor in actors:
    print(f"{actor.title()}, you did great!")
print("\n")

# range loops
for i in range(1, 6):
    print(i)

# create a list of numbers using range
numbers = list(range(0, 20))
print(numbers)

numbers = list(range(0, 201, 20))
print(numbers)

square = []
for i in range(11):
    square.append(i ** 2)

print(square)

# list comprehension
squares = [value**2 for value in range(1, 6)]
print(squares)






