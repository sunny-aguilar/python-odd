
# name = 'sandro'
# age = 37
# print(name, end=' ')
# print(age)
#
# print(1,2,3,4,5,sep='*')
#
# print(format(232.1482224, '9,.2f'))
#
# if 'Sandro' is 'Sandro':
#     print('equivalent')
#
# if 5 > 2:
#     print('yay!')


# #x = input('Enter a number for x: ')
# #y = input('Enter a number for y: ')
#
# if x > y:
#     print('X is greater')
# elif x < y:
#     print('Y is greater')
# else:
#     print('X and Y are equal to each other')
#
# if 10 == 10 and 1 == 1:
#     print('They are both equal')
#
# if 2 is 2 and 3 is 3:
#     print('Both are equal')

# x = 10
# while x > 0:
#     print(x, ' is the current value.')
#     x = x - 1

# sales_met = True
#
# if sales_met:
#     print('sales quota has been met')
#
#
# if 100 > 0 and 22 < 1000:
#     print('that is correct!')
#

# for row in range(8):
#     for col in range(6):
#         print('*', end='')
#     print()


# def main():
#     createfile()
#
# def createfile():
#     my_file = 'dataFile.txt'
#     infile = open(my_file, 'w')
#     infile.write('My first Python written text file\n')
#     infile.write('more text\n')
#     infile.write('and some more text\n')
#     infile.close()
#
# main()
#
#
# myList = [11, 12, 13, 14, 15]
# nameList = ['Sunny', 'Jese', 'Wesley']
#
# for x in nameList:
#     print(x)


# myList = ['Sunny'] * 5
# print(myList)
# listLength = len(myList)
# print(listLength)

# mylist = ['a', 'b', 'c', 'd', 'e']
# print(mylist[:3])


# if 'z' in mylist:
#     print('value found')
# else:
#     print('value not found')

# mylist = [4, 3, 8, 2, 1, 9, 0, 6, 5, 7]
# print(mylist)
# mylist.append(11)
# print(mylist)
# mylist.insert(0, 100)
# print(mylist)
# mylist.sort()
# print(mylist)
# mylist.remove(100)
# print(mylist)
#
#
# mylistcopy = [] + mylist
# mylist.append(12)
# print(mylist)
# print(mylistcopy)


# modifying print newline function
# matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
# for r in range(3):
#     for c in range(3):
#         print(matrix[r][c], end=' ')
#
# print()
#
# for r in range(3):
#     for c in range(3):
#         print(matrix[r][c], end=', ')
#
# print()
#
# for r in range(3):
#     for c in range(3):
#         print(matrix[r][c], end='-')

# myName = 'Sandro'
# newName = ''
# for x in myName:
#     newName += x
#
# print(newName)

# myName = 'Sandro Aguilar'
# for ch in myName:
#     if ch == 'a' or ch == 'r':
#         print('Character found')


# myName = '1200'
# print(myName.isdigit())


# dictionaries

# phonebook = {
#     'Sunny': '916-735-6948',
#     'Wesley': '916-908-7266',
#     'Crystal': '622-888-8888'
# }
# if 'Joe' in phonebook:
#     print(phonebook['Sunny'])
# else:
#     print("key not found")

# for x in phonebook:
#     print(phonebook[x])

# for x, y in phonebook.items():
#     print(x, y)

# or
# for key in phonebook:
#     print(key, phonebook[key])

# for key in phonebook.values():
#     print(key)

# value = phonebook.get('Jack', 'Value not found')
# print(value)
# a = 1
# b = 3
# print(a, b)
# a, b = b, a
# print(a, b)


# class Sandro:
#     def __init__(self):
#         self.name = 'Sandro'
#
#     def printName(self):
#         print(self.name, ', you have just created a python class')
#
#     def changeName(self):
#         self.name = input('Enter a new name: ')
#
#
# myClass = Sandro()
# myClass.printName()
# myClass.changeName()
# myClass.printName()





#importing a class
import module

# main program
def main():
    my_coin = module.Coin()

    print('This side is up: ', my_coin.get_sideup())
    print('I am tossing the coin ...')

    my_coin.toss()
    my_coin.__sideup = 'Heads'      # no longer works! its private now bitches

    # print('I am going to toss the coin ten times:')
    # for count in range(10):
    #     my_coin.toss()
    #     print(my_coin.get_sideup())
    flip(my_coin)

    # __str__ method by passing an object to the
    # print function
    print(my_coin)


def flip(coin_object):
    coin_object.toss()


main()
