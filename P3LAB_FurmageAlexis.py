#Alexis Furmage
#10/14/2024
#This program allows the user to enter a money (float) value with two places after the decimal.

"""
Pseudocode:
1. Define a function calculate_coins(amount):
   a. If amount is 0.00:
      i. Print "No change"
      ii. Return (exit function)
   
   b. Convert amount to cents by multiplying by 100 and converting to integer.
   c. Initialize coin values (dollar, quarter, dime, nickel, penny) in cents.
   
   d. Calculate the number of each coin:
      i. Calculate dollars using floor division (total cents // dollar value).
      ii. Update total cents to the remainder (total cents % dollar value).
      iii. Repeat for quarters, dimes, nickels, and pennies.
   
   e. For each coin type, if the count is greater than 0:
      i. Print the number of coins with the correct singular/plural form.
   
2. Get user input as a float for the amount.
3. Call calculate_coins() with the user input amount.
"""



def calculate_coins(amount):
    if amount == 0.00:
        print("No change")
        return

    total_cents = int(amount * 100)

    
    dollar_value = 100
    quarter_value = 25
    dime_value = 10
    nickel_value = 5
    penny_value = 1

   
    dollars = total_cents // dollar_value
    total_cents %= dollar_value
    
    quarters = total_cents // quarter_value
    total_cents %= quarter_value
    
    dimes = total_cents // dime_value
    total_cents %= dime_value
    
    nickels = total_cents // nickel_value
    total_cents %= nickel_value
    
    pennies = total_cents // penny_value
    
   
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")


amount = float(input("Enter the amount of money as a float: $"))
calculate_coins(amount)
