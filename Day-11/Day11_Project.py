#Project Day 11
import random

#clear terminal
#---------------------------------------------
import os
def clear():
    os.system('cls')
#---------------------------------------------

#------------------------------------------------------------------
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
#------------------------------------------------------------------

cards=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
card_values={"A":11,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"J":10,"Q":10,"K":10}
suits=["Spades","Hearts","Clubs","Diamonds"]

def new_deck():
    deck=[]
    for suit in suits:
        for card in cards:
            deck.append({'suit':suit,'card':card,'card value':card_values[card]})
    return deck

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  elif user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 21:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 21:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def black_jack(deck):
    player_cards=[]
    computer_cards=[]
    player_score=0
    computer_score=0
    game_over= False

    def get_details():
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

    #player dealing
    while len(player_cards)<2:
        player_card=random.choice(deck)
        player_cards.append(player_card['card value'])
        deck.remove(player_card)
        player_score+=player_card['card value']
        if(player_score>21):
            player_cards[1]=1
            player_score-=10

    #computer dealing
    while len(computer_cards)<2:
        computer_card=random.choice(deck)
        computer_cards.append(computer_card['card value'])
        deck.remove(computer_card)
        computer_score+=computer_card['card value']
        if(computer_score>21):
            computer_cards[1]=1
            computer_score-=10

    get_details()
    while not game_over:
        if player_score == 21 or computer_score == 21 or player_score > 21:
            break
        get_card=input("Type 'y' to get another card, type 'n' to pass: ")
        if(get_card=='y'):
            player_card=random.choice(deck)
            deck.remove(player_card)
            if(player_score+player_card['card value']>21 and player_card['card value']==11):
                player_cards.append(1)
                player_score+=1
            else:
                player_cards.append(player_card['card value'])
                player_score+=player_card['card value']
        else:
            break
        get_details()
    
    while computer_score<17 and player_score<22:
        if player_score == 21 or computer_score == 21 or player_score > 21 :
            break
        else:
            computer_card=random.choice(deck)
            deck.remove(computer_card)
            if(computer_score+computer_card['card value']>21 and computer_card['card value']==11):
                computer_cards.append(1)
                computer_score+=1
            else:
                computer_cards.append(computer_card['card value'])
                computer_score+=computer_card['card value']
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score,computer_score))


play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play.lower()=='y':
    clear()
    print(logo)
    black_jack(new_deck())
    play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
