
# to get random numbers
import random

class Coin:
    def __init__(self):
        self.__sideup = 'Heads'
        self.__value = 7

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup

    def __str__(self):
        return 'The coin is currently ' + self.get_sideup() + ' up.'




