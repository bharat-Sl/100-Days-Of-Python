#Project Day14
from game_data import data
import art
import random

#clear terminal
#---------------------------------------------
import os
def clear():
    os.system('cls')
#---------------------------------------------

def game():
    List=data
    score=0
    end=False
    print(art.logo)
    choice1=random.choice(List)
    List.remove(choice1)
    while not end:
        choice2=random.choice(List)
        List.remove(choice2)
        print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}.")
        print(art.vs)
        print(f"Compare B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}.")
        choice=input("Who has more followers? Type 'A' or 'B': ").lower()
        if(choice1['follower_count']>choice2['follower_count'] and choice=='a'):
            clear()
            score+=1
            print(art.logo)
            print(f"You're right! Current score: {score}.")
            choice1=choice2 
        elif(choice1['follower_count']<choice2['follower_count'] and choice=='b'):
            clear()
            score+=1
            print(art.logo)
            print(f"You're right! Current score: {score}.")
            choice1=choice2  
        else:
            clear()
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            return

game()
