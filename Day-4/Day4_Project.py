#Project Day4
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
List=[rock,paper,scissors]

print("Welcome to a quick mach of Rock, Paper and Scissors")
user_choice=int(input("What do you choose?\nType 1 For Rock.\nType 2 For Paper.\nType 3 For Scissors.\n"))-1
if (user_choice>3 or user_choice<1):
    print('Wrong input recieved')
else:
    print(f'\n\nYou chose:{List[user_choice]}')
    computer_choice=random.randint(0,2)
    print(f'\n\nComputer chose:{List[computer_choice]}')
    choice=user_choice-computer_choice
    if(choice==0):
        print('Its a draw.')
    elif(choice==1 or choice==-2):
        print('You won.')
    else:
        print('You Lost.')