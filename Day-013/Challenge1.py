#challenge 1
#To find all bugs in below code

#------------------------------------------------------------------
# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")
#------------------------------------------------------------------

#the error arises in if, condition check refers to assignment operator
#The correct code is.


number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  

