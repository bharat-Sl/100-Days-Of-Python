#
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total_characters=nr_letters+nr_symbols+nr_numbers
choosen=[]
password=''
for i in range(0,total_characters):
    if(nr_letters>0):
        choosen.append(letters[random.randint(0,len(letters))])  
        nr_letters-=1
    if(nr_numbers>0):
        choosen.append(numbers[random.randint(0,len(numbers))])
        nr_numbers-=1
    if(nr_symbols>0):
        choosen.append(symbols[random.randint(0,len(symbols))])  
        nr_symbols-=1
for i in range(0,total_characters):
    password+=choosen.pop(random.randint(0,len(choosen)-1))
print(f"Here is your password:{password}")