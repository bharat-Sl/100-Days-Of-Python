#challenge 2
import math

#function defination
def prime_checker(number):
    flag=1
    for i in range(2,number):
        if number%i==0:
            flag=0
            break
    if(flag==1):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Driver Code#
#-----------------------------------------------------------
n = int(input("Check this number: "))
prime_checker(number=n)
#-----------------------------------------------------------