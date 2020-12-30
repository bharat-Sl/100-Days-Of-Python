#Project Day9

#clear terminal
#---------------------------------------------
import os
def clear():
    os.system('cls')
#---------------------------------------------


# Project Art
#---------------------------------------------
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
#---------------------------------------------

people_list=[]
more=True
print(logo)
print("Welcome to the secret auction program.")
while more:
    name=input('What is your name?: ')
    bid=int(input('What\'s your bid?: Rs'))
    other=input('Are there any other bidders? Type \'yes\' or \'no\'.\n')
    people_list.append({"Name":name,"Bid":bid})
    if(other.lower()=='no'):
        more=False
    clear()

max_name=''
max_bid=0
for people in people_list:
        if(people['Bid']>max_bid):
            max_name=people['Name']
            max_bid=people['Bid']


print(f'The winner is {max_name} with a bid of Rs{max_bid}.')
