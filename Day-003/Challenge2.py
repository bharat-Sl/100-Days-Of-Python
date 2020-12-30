#challenge 2
height=float(input("Enter your height in cm:"))
weight=float(input("Enter your weight in kg:"))

BMI=weight/(height/100)**2
if BMI<18.5:
    print("You are underweight.")
elif BMI<25:
    print("You have a normal weight.")
elif BMI<30:
    print("You are overweight.")
elif BMI<35:
    print("You are obese.")
else:
    print("You are clinically obese. Concern a doctor immediately.")