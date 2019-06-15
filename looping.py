"""
" Mulitline comment
"""
# mylist = [1, 2, 3, 4, 5, 6]
# print(mylist)
# mylist.remove(1)
# print(mylist)
#
# x = mylist.pop(2)
# print(mylist)
# print(x)

list_one = [0, 1, 2, 3, 4, 5]
list_two = [5, 6, 7, 8, 9]

# add two lists together
list_one.extend(list_two)
print(list_one)

# insert(where, what)
list_one.insert(0, "Sandro")
print(list_one)
