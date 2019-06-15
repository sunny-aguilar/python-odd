phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
# ['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']
# convert to "on tap"

for i in range(4):
    plist.pop()
plist.pop()
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])