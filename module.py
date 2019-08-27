
#importing a class
import coin



def main():
    my_coin = coin.Coin()
    print('This side is up: ', my_coin.get_sideup())
    print('I am tossing the coin ...')
    my_coin.toss()
    my_coin.__sideup = 'Heads'      # no longer works! its private now bitches

    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

main()