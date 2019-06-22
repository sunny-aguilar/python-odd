"""files and exceptions"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

with open('pi_digits.txt') as file_object:
    mylist = file_object.readlines()

print(mylist)

with open('pi_million_digits.txt') as file_object:
    mylist = file_object.readlines()

pi_string = ''
for line in mylist:
    pi_string += line.strip()



