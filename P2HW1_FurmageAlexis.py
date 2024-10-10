# Alexis Furmage
# 09-24-24
# P2HW1
# This program calculates and displays travel expenses with nicely formatted output.
"""
Pseudocode:
1. Start program
2. Print a welcome message
3. Prompt the user to enter their budget and store it in 'budget'
4. Prompt the user to enter their travel destination and store it in 'destination'
5. Prompt the user for estimated fuel costs and store it in 'fuel'
6. Prompt the user for estimated accommodation costs and store it in 'accommodation'
7. Prompt the user for estimated food costs and store it in 'food'
8. Calculate the total expenses by adding fuel, accommodation, and food
9. Calculate the remaining balance by subtracting total expenses from the budget
10. Display the travel expenses details including:
    - Location
    - Initial Budget
    - Fuel costs
    - Accommodation costs
    - Food costs
    - Remaining Balance
11. End program
"""

def calculate_travel_expenses():
    print("This program calculates and displays travel expenses\n")
    
    budget = float(input("Enter Budget: "))
    destination = input("Enter your travel destination: ")
    fuel = float(input("How much do you think you will spend on gas? "))
    accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
    food = float(input("Last, how much do you need for food? "))
    
    # Calculate total expenses and remaining balance
    total_expenses = fuel + accommodation + food
    remaining_balance = budget - total_expenses

    # Print the formatted output
    print("\n------------ Travel Expenses ------------")
    print(f"{'Location:':<20} {destination}")
    print(f"{'Initial Budget:':<20} ${budget:,.2f}")
    print(f"{'Fuel:':<20} ${fuel:,.2f}")
    print(f"{'Accommodation:':<20} ${accommodation:,.2f}")
    print(f"{'Food:':<20} ${food:,.2f}")
    print("------------------------------------------")
    print(f"{'Remaining Balance:':<20} ${remaining_balance:,.2f}")

if __name__ == "__main__":
    calculate_travel_expenses()

