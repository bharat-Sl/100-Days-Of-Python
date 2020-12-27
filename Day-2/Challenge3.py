#challenge 3
age=input("what is your current age?\n")
years_left=90-int(age)
months_left=years_left*12
days_left=years_left*365+int(years_left/4)
weeks_left=days_left/7
print(f"You have {int(days_left)} days,{int(weeks_left)} weeks,{int(months_left)} months left.")