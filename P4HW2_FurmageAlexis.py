# Alexis Furmage
# 11/1/24
# P4HW2
# Assignment assess student ability to edit and enhance exiting programs


"""
BEGIN PROGRAM

    INITIALIZE total_employees = 0
    INITIALIZE total_regular_pay = 0
    INITIALIZE total_overtime_pay = 0
    INITIALIZE total_gross_pay = 0

    WHILE True
        PROMPT user for employee's name or 'Done' to terminate
        IF name is "Done"
            BREAK

        PROMPT for hours worked
        PROMPT for pay rate

        IF hours_worked > 40
            CALCULATE regular_pay = 40 * pay_rate
            CALCULATE overtime_hours = hours_worked - 40
            CALCULATE overtime_pay = overtime_hours * (pay_rate * 1.5)
            CALCULATE gross_pay = regular_pay + overtime_pay
        ELSE
            CALCULATE regular_pay = hours_worked * pay_rate
            SET overtime_pay = 0
            SET gross_pay = regular_pay

        UPDATE totals
        INCREMENT total_employees by 1
        ADD regular_pay to total_regular_pay
        ADD overtime_pay to total_overtime_pay
        ADD gross_pay to total_gross_pay

        DISPLAY employee's information including hours worked, pay rate, overtime hours, overtime pay, regular pay, and gross pay

    FINAL SUMMARY OUTPUT
    PRINT total number of employees entered
    PRINT total amount paid for overtime
    PRINT total amount paid for regular hours
    PRINT total amount paid in gross

END PROGRAM
"""

# Your Name
# Date
# Assignment: P4HW2
# Description: This program calculates the gross pay for multiple employees, including overtime and regular pay, 
# and provides a summary of total amounts paid.

# Initialize totals
total_employees = 0
total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0

while True:
    # Ask for employee's name
    name = input("Enter employee's name or 'Done' to terminate: ")
    if name == "Done":
        break

    # Input hours and pay rate
    hours_worked = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))

    # Calculate pay
    if hours_worked > 40:
        regular_pay = 40 * pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        gross_pay = regular_pay + overtime_pay
    else:
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0
        gross_pay = regular_pay

    # Update totals
    total_employees += 1
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay

    # Display individual employee's information
    print("\nEmployee name:", name)
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
    print("-" * 70)  # Print a line of dashes for separation
    print(f"{hours_worked:<15.1f} {pay_rate:<10.2f} {overtime_hours if hours_worked > 40 else 0:<10.1f} {overtime_pay:<15.2f} {regular_pay:<12.2f} {gross_pay:<10.2f}\n")

# Final summary output
print(f"\nTotal number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

