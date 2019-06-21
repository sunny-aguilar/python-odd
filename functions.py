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




