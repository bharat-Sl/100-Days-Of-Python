#challenge 4
print("Welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want? S, M, or L\n")
pepperoni=input("Do you want pepperoni?Y or N\n")
cheeze=input("Do you want extra cheese? Y or N\n")
price=0.0
if size=='S': 
    price=140
elif size=='M':
    price=260
elif size=='L':
    price=400
else:
    print("Wrong Input recieved. Please try again")
if pepperoni=='Y':
    if size=='S':
        price+=65
    elif size=='M' or size=='L':
        price+=100
if cheeze=='Y':
    price+=30
print(f'Your final bill is: Rs{price}')