import random


def game():

    countery = 0
    counterb = 0
    print('Stone, Paper or Scissors\nFor exit, enter (Break)')
    while True:

        print('counter: {0}/{1}'.format(countery, counterb))
        a = input('Enter: ')
        k = ['Stone', 'Paper', 'Scissors']
        o = random.choice(k)

        if a == 'Break':
            print('Stop')
            return 'Stop'

        if a == 'Stone':

            if o == 'Stone':
                print('Stone')
                print('Draw')

            if o == 'Paper':
                print('Paper')
                print('You loose')
                counterb += 1

            if o == 'Scissors':
                print('Scissors')
                print('You win')
                countery += 1

        if a == 'Paper':

            if o == 'Stone':
                print('Stone')
                print('You win')
                countery += 1

            if o == 'Paper':
                print('Paper')
                print('Draw')

            if o == 'Scissors':
                print('Scissors')
                print('You loose')
                counterb += 1

        if a == 'Scissors':

            if o == 'Stone':
                print('Stone')
                print('You loose')
                counterb += 1

            if o == 'Paper':
                print('Paper')
                print('You win')
                countery += 1

            if o == 'Scissors':
                print('Scissors')
                print('Draw')

        if a != 'Stone' and a != 'Paper' and a != 'Scissors':
            print('Error!')
            return 'Error'


game()
