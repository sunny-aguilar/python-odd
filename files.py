"""files and exceptions"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

with open('pi_digits.txt') as file_object:
    lylist = file_object.readlines()


