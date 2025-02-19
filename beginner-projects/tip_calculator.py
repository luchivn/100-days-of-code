print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? %"))
people = int(input("How many people are splitting the bill? "))

if tip == 10 or tip == 12 or tip == 15:
  total_bill = total_bill + (tip/100)*total_bill
  bill = total_bill / people
  print("Each person should pay: $", bill)
else:
  print("Invalid tip input!")
