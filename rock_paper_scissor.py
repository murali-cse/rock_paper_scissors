import random
import os
from ascii_art import *

# choices
choices = ['rock', 'paper', 'scissors']

# choices dictonary
choice_dic = {
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}

computer = random.choice(choices)

ans = True

while(ans):
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')    

    # get the choice from the user
    user = input('\nChoose your choice\nr= Rock\np= Paper\ns= Scissors\n')
    if user in choice_dic:
        ans= False
        user = choice_dic[user]
        print('\n================================================\n')
        print(f'You Chose : {user}\n')
        print(f'Computer Chose : {computer}\n')
        if user == computer:
            print(f'You both selected {user}, its tie!')
        elif user == 'rock':
            if computer == 'paper':
                print(left_rock+" "+right_paper)
                print('Paper covers rock, Computer wins!')
            elif computer == 'scissors':
                print(left_rock+" "+right_scissors)
                print('Rock smashes scissors, You wins!')
        elif user == 'paper':
            if computer == 'rock':
                print(left_paper+" "+right_rock)
                print('Paper covers rock, You wins!')
            elif computer == 'scissors':
                print(left_paper+" "+right_scissors)
                print('Scissors cuts paper, Computer wins!')
        elif user == 'scissors':
            if computer == 'rock':
                print(left_scissors+" "+right_rock)
                print('Rock smashes scissors, Computer wins!')
            elif computer == 'paper':
                print(left_scissors+" "+right_paper)
                print('Scissors cuts paper, You wins!')

        print('\n================================================')
    else:
        print("Invalid choice. Please choose again.")

