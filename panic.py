# Author:           Sandro Aguilar
# Date:             June 17, 2019
# Description:      Python program

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
# what prints
# ['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']
# convert to "on tap"

new_phrase = ''.join(list(plist[1:3:1])) \
             + ''.join(list(plist[5:6:1])) + ''.join(list())
             + ''.join(list(plist[7:5:-1]))

# for i in range(4):
#     plist.pop()
# plist.pop(0)
# plist.remove("'")
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))

# new_phrase = ''.join(plist)
# print(plist)
print(new_phrase)
# myName = "Sandro Aguilar lives in Roseville"
# myList = list(myName)
#
# print(''.join(myList[::2]))
# print(''.join(myList[13:6:-1]))