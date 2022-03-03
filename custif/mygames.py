#!/usr/bin/env python3
"""TPatrick | Alta3
   Making my own custom if script!"""

def games():

    # The first part of our message, regardless of difficulty   
    message = 'I\'d like to make a gaming recommendation! '
    
    # Defining difficulty as a Float based on user input
    difficulty = float(input("On a scale of 1 to 10, how difficult do you like your games to be? "))
    
    # Our Custom if, which is sure to be scathing for some
    if difficulty >= 9001:
        message = 'Ok, ok. Calm down Vegeta.'
    elif difficulty >= 10:
        message = message + 'You\'re crazy enough for Elden Ring!'
    elif difficulty >= 7:
        message = message + 'Try playing Lost Ark!'
    elif difficulty >= 3:
        message = message + 'Try playing FFXIV!'
    elif difficulty <=  2:
        message = message + 'Huh, I suppose Helly Kitty Island is a thing.'
    
    # Pushing result to stdout.
    print(message)

if __name__ == "__main__":
    games()
