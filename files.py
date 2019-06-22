"""files and exceptions"""

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)
#
# with open('pi_digits.txt') as file_object:
#     mylist = file_object.readlines()
#
# print(mylist)

# checking if bday is in pi
# with open('pi_million_digits.txt') as file_object:
#     mylist = file_object.readlines()
#
# pi_string = ''
# for line in mylist:
#     pi_string += line.strip()
#
# birthday = input('Enter your bday in mmddyy format: ')
# if birthday in pi_string:
#     print('Your birthday is in pi!')
# else:
#     print('Your bday is not in pi :(')

# writing to a file
# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
#     file_object.write('I love programming!\n')
#     file_object.write('I like creating games')


# try/except blocks
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Cannot divide by zero")


# count characters in file
filename = "pi_million_digits.txt"
with open(filename) as filename:
    contents = filename.read()

chars = list(contents)
char_length = len(chars)
print(char_length)


