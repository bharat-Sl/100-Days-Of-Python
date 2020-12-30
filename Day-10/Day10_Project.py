#Project Day3

#clear terminal
#---------------------------------------------
import os
def clear():
    os.system('cls')
#---------------------------------------------

#------------------------------------------------------------------------------------------------------------
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
#------------------------------------------------------------------------------------------------------------

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

operands=['+','-','*','/']
operations={'+':add,'-':subtract,'*':multiply,'/':divide}

def calc(num1,num2,operation):
    s=0.0
    func=operations[operation]
    s=func(num1,num2)
    s=round(s,3)
    print(f'{num1} {operation} {num2} = {s}')
    return s

print(logo)
first_num=float(input("What's the first number?: "))
print('+\n-\n*\n/')
end=False
while not end:
    operation=input("Pick an operation: ")
    if(operation not in operands):
        print('Operand not recognised. Please re-enter.')
        continue
    second_num=float(input("What's the next number?: "))
    first_num=calc(first_num,second_num,operation)

    choice=input(f"Type 'y' to continue calculating with {first_num},\nor type 'n' to start a new calculation,\nor type 'exit' to exit: ")
    if(choice.lower()=='n'):
        clear()
        print(logo)
        first_num=float(input("What's the first number?: "))
    elif(choice.lower()=='exit'):
        end=True