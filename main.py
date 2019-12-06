import math 
number = float(input("please enter a number:"))
result = math.sqrt(number)
print("square root of ", number, " is: ", result)
yes = input("would you like to type a new number?")
type(yes)
if (yes=="no"):
  print("ok. have a good day!")
if (yes=="yes"):
 number = float(input("please enter a number:"))
 result = math.sqrt(number)
print("square root of ", number, " is: ", result)





