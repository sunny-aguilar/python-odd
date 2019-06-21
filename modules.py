# import entire module
import my_module
my_module.say_hello('sandro')

# using aliases for module
import my_module as mm
mm.say_hello('sandro')

# import specific functions from modules
from my_module import say_hello, say_age
say_hello('sandro')
say_age(37)

# using aliases for functions
from my_module import say_hello as hp, say_age as sa
hp('sandro')
sa(37)

# import all functions from module
from my_module import *
say_hello('sandro')
say_age(37)



