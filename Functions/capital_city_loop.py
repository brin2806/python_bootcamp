from capitals import capitals_dict
import random

'''
use a while loop to iterate through a dictionary and grab a\n
random state & capital \n
'''

random_state = random.choice(list(capitals_dict.keys()))
capital = capitals_dict[random_state]

while True:   # create an infite loop
    capital_guess = input("What is the capital of {} : ".format(random_state)).lower()

    if capital_guess == "exit":
        print("The capital of {} is {}".format(random_state, capital))
        print("goodbye")
        break

    elif capital_guess == capital.lower():
        print("Correct")
        break





#assign each randon state/capital pair to a variable
#ask user for capital of state randomly picked
#infite loop asking for capital till answer correctly or types 'exit'
#display 'Correct' if answered correctly after loop ends
#display 'goodbye' if ext game
# do not punish for casesensitivity
