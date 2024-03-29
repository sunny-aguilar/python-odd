alien_0 = {
    'color': 'green',
    'points': 5
}

# print single elements from dictionary
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

# add additional values to dictionary
alien_0['eyes'] = 4
alien_0['name'] = 'Bob'
print(alien_0)

# empty dictionary
alien = {}
alien['age'] = 20
alien['name'] = "Bob"
alien['speed'] = "fast"
print(alien)
del alien['speed']
print(alien)

points = alien.get('points', "no points have been set")
print(points, '\n')

# .items() looping through dictionary
user = {
    'username': "vluedevil",
    'first': 'sandro',
    'last': 'aguilar',
    'age': 'thirty seven',
}

for key, value in user.items():
    print(f"\nkey: {key}")
    print(f"Value: {value}")
print('\n')

# .keys() method
for key in user.keys():
    print(key.title())
print('\n')

# not in key
if 'attitude' not in user.keys():
    print("Nice attitude Sandro!")
print('\n')

# .values() method
for values in user.values():
    print(values.title())
print('\n')

#


