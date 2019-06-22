"""files and exceptions"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

with open('pi_digits.txt') as file_object:
    mylist = file_object.readlines()

print(mylist)

with open('pi_million_digits.txt') as file_object:
    mylist = file_object.readlines()


for line in mylist:

