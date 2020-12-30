#Project Day3
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,="     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--"___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
Action=input('Entering the great forest of Juna You come to a split in the path. Do you go Left or Right?\n')
if(Action.lower()=='left'):
    Action=input('There is a River up ahead. It seams calm enough to swim. Do you \'Wait\' for a raft or \'Swim\' across?\n')
    if Action.lower()=='wait':
        Action=input("You waited for the raft and crossed the river safely. You now observe three doors leading to nowhere. You must open one! Choose between 'Red','Yellow' and 'Green'.\n")
        if(Action.lower()=='red'):
            print('As you opened the door, the door burst into flames killing you that instant. Game Over.')
        elif(Action.lower()=='yellow'):
            print('As you opened the door and stepped in, the floor collapsed and you fall to your death. Game Over.')
        elif(Action.lower()=='green'):
            print("The treasure gleamed with the sunlight entering in the room. You won.")
    else:
        print('You were bitten by a poisionous river snake and died as you crossed the river. Game Over.')
else:
    print('You fell in a hole. Game Over.')