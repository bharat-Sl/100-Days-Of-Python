#challenge 3
year =int(input("Which year do you want to check?"))
if year%4==0 and year%100!=0:
    print("It is a Leap year!")
elif year%100==0 and year%400==0:
    print("It is a Leap year!")
else:
    print("It is not a Leap year.")