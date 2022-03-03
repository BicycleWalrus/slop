#!/usr/bin/env python3

round = 0
answer = " "

while round < 3 and answer.lower() != "brian":
    round = round + 1
    print('Finish the movie title, "Monthy Python\'s The Life of ______"')
    answer = input("Your guess---> ")
    if answer.lower() == 'brian':
        print('Correct!')
    elif round == 3:
        print('Sorry, the answer was Brian.')
    elif answer.lower() == 'shrubbery':
        print('You found the secret answer!')
        break
    else:
        print('Sorry. Try again!')
