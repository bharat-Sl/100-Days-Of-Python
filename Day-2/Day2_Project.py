#Project Day2
print("Welcome to the tip calculator.")
Bill=int(input("What was the total bill? Rs"))
tip=int(input("What percentage tip would you like to give?  "))
people=int(input("How many people to split the bill? "))
each=(Bill+tip*Bill/100)/people
print(f"Each person should pay: Rs{round(each,2)}")