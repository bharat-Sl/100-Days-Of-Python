#challenge 2
import random
People=input("Enter names of everyone seperated by comma.\n").split(',')
random_pick=random.randint(0,len(People)-1)
#random_pick=random.choice(People)
print(f"{People[random_pick]} is going to buy the meal today")