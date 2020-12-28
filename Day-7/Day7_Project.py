import random
import Hangman_Art
from Word_List import word_list

def check(cha,lis):
    flag=True
    for i in lis:
        if(i==cha):
            return False
    return flag

def main_check(cha,lis):
    flag=False
    for i in lis:
        if(i==cha):
            return True
    return flag

def main_game(selected_word,word_letters):
    life=7
    finish=False
    user_entered_list=[]
    while life>0 and finish!=True:
        char=input('\nGuess the Character:')
        if char.isalpha:
            if check(char,user_entered_list):
                user_entered_list.append(char)
                if(main_check(char , word_letters)):
                    print('Great Choice! You guessed right!')
                    if(all(item in user_entered_list for item in word_letters)):
                        finish=True
                        break
                else:
                    life-=1
                    print(Hangman_Art.stages[life])
                    print(f'Wrong guess. You lost a Life. {life} Tries Left')
            else:
                print('The Character has already been guessed.')
                print('\n')
            for i in word_letters:
                if i!=' ' and i in user_entered_list:
                    print(i+' ',end='')
                elif i==' ':
                    print('  ',end='')
                else:
                    print('_ ',end='')
        else:
            print('wrong input recieved! Retry')
    if(life>0 and finish==True):
        print(f'\n\nYou got it right! The word was {selected_word}')
    else:
        print(f'\n\n[You Lost]\nThe word was {selected_word} ')


#----------------------------------------------------------------------------------------------------
selected_word=random.choice(word_list)
word_letters=list(selected_word)
print(Hangman_Art.logo)
print('Welcome to Hangman! Save the stickman from hanging by completing the word.')
print('\nThe word to guess: ')
for i in word_letters:
    if i!=' ':
        print('_ ',end='')
main_game(selected_word,word_letters)

#-----------------------------------------------------------------------------------------------------