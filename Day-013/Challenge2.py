#challenge 2
#To find all bugs in below code

#------------------------------------------------------------------
# year = input("Which year do you want to check?")

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

#------------------------------------------------------------------

#the error arises in variable year as the input recived from the user is a string and we need a integer value
#The correct code is.

year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  