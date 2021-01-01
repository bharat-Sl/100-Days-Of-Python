#Project Day9
import random

#----------------------------------------------------------------------------------------
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
#----------------------------------------------------------------------------------------

def guess_number(chances):
    r_number=random.randint(1,100)
    flag=0
    while chances>0:
        print(f'You have {chances} attempts remaining to guess the number.')
        guess=int(input('Make a guess: '))
        if(guess==r_number):
            print('You got it right!')
            flag=1
            break
        elif(guess>r_number):
            print("Too high.")
            chances-=1
        else:
            print("Too low.")
            chances-=1
    if(flag==0 and chances==0):
        print("You've run out of guesses, you lose.")

print(logo)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if(difficulty.lower()=='easy'):
    guess_number(10)
elif(difficulty.lower()=='hard'):
    guess_number(5)
else:
    print("Wrong input recieved!")