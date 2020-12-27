#challenge 1
import random
flip=random.randint(0,1)
choice=input('Heads or tails? Enter your choice:')
if flip==1:
    if choice=='heads':
        print('Its Heads! You won.')
    else:
        print('Its Tails. You Lost.')
else:
    if choice=='tails':
        print('Its Tails! You won.')
    else:
        print('Its Heads. You Lost.')