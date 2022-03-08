#!/usr/bin/env python3

"""TPatrick | Alta3 Research
   Running a simulation with our classes"""

from cheatdice import *

def main():
    """called at runtime"""

    swapper = Cheat_Swapper()
    loaded_dice = Cheat_Loaded_Dice()

    swapper_score = 0
    loaded_dice_score = 0

    number_of_games = 100000
    game_number = 0

    print("Simulation Running!")
    print("===================")

    while game_number < number_of_games:
        swapper.roll()
        loaded_dice.roll()

        swapper.cheat()
        loaded_dice.cheat()

        if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
            pass
        elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
            swapper_score += 1
        else:
            loaded_dice_score += 1
        game_number += 1

    print("Simulation complete")
    print("-------------------")
    print("Final Scores")
    print("-------------------")
    print(f"Swapper won: {swapper_score}")
    print(f"Loaded dice won: {loaded_dice_score}")

    if swapper_score == loaded_dice_score:
        print("Game was drawn")
    elif swapper_score > loaded_dice_score:
        print("Swapper won most games")
    else:
        print("Loaded dice won most games")

if __name__ == "__main__":
    main()
