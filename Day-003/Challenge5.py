#challenge 5
print("Welcome to the Love Calculator!")
name1=input("What is your name? \n")
name2=input("What is their name? \n")
name=name1.lower()+name2.lower()
t=name.count('t')
r=name.count('r') 
u=name.count('u')
e=name.count('e')
l=name.count('l')
o=name.count('o')
v=name.count('v')
e=name.count('e')
true=t+r+u+e
love=l+o+v+e
percentage=true*10+love
if percentage>90 or percentage<10:
    print(f'Your Score is {percentage}, you go together like coke and mentos.')
elif percentage>40 and percentage<50:
    print(f'Your Score is {percentage}, you are alright together.')
else: 
    print(f'Your Score is {percentage}.')