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
print(points)

user = {
    'username': "vluedevil",
    'first': 'sandro',
    'last': 'aguilar'
}


