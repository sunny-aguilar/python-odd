# functions
def hello(name="nameless"):
    """say hi"""
    print(f"Hello! {name.title()}")


# normal function call
hello("Wesley")
# keyword arguments
hello(name="sandro")
# default values
hello()
print('\n')

def sayname(first, last):
    yourname = f"{first} {last}"
    return yourname.title()


name = sayname("sandro", "aguilar")
print(name)

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

programmer = build_person("sandro", "aguilar", 37)
print(programmer)
print('\n')

def multiple_values(*values):
    print(values)

multiple_values('honda', 'ford', 'BMW')
multiple_values('chevy')


