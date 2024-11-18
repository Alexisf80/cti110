#Alexis Furmage
#11/08/2024
#P5LAB
#This program will simulate a customer using a self-checkout machine. A random float value will be generated as the total owed for the purchase. The program should then display the amount of dollars, quarters, dimes, nickels, and pennies required to make the change.

"""
Pseudocode:

1. Import the random module to generate a random purchase amount.

2. Define a function called disperse_change(change):
   a. If change is 0.00:
      i. Print "No change" and exit the function.
   
   b. Convert the change amount from dollars to cents for easier calculation.
   
   c. Define the values of each coin type (dollars, quarters, dimes, nickels, and pennies) in cents.
   
   d. Calculate the number of each coin type needed to make the change:
      i. Use floor division to determine the number of dollars (total cents // dollar value).
      ii. Update the remaining cents to be the remainder after removing dollars.
      iii. Repeat the process for quarters, dimes, nickels, and pennies.
   
   e. For each coin type, if the count is greater than 0:
      i. Print the number of coins needed, adjusting for singular or plural as necessary.

3. Define the main function:
   a. Generate a random amount owed by the customer using a float between 0.01 and 100.00, rounded to 2 decimal places.
   b. Display the amount owed to the user.
   
   c. Prompt the user to enter the cash amount they will put into the self-checkout.
   
   d. Calculate the change owed to the customer by subtracting the amount owed from the cash provided.
   
   e. Display the calculated change.
   
   f. Call the disperse_change function, passing in the change as an argument to break it down into coin values.

4. Call the main function to execute the program.
"""

import random

def disperse_change(change):
    if change == 0.00:
        print("No change")
        return

    total_cents = int(change * 100)

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

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed}")

    cash_provided = float(input("How much cash will you put in the self-checkout? "))
    
    change = round(cash_provided - amount_owed, 2)
    print(f"Change is: ${change}\n")

    disperse_change(change)

if __name__ == "__main__":
    main()
