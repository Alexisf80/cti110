# Alexis Furmage
#10/24/24
# P3HW2
# Creating a program calculates the pay for an employee based on hours worked, pay rate, and overtime.

def calculate_pay():
    """
    Pseudocode:
    
    FUNCTION calculate_pay:
        1. PROMPT user to enter employee's name
        2. PROMPT user to enter number of hours worked
        3. PROMPT user to enter employee's pay rate
        
        4. INITIALIZE overtime_hours to 0
        5. IF hours_worked > 40:
            a. SET overtime_hours to hours_worked - 40
            b. SET regular_hours to 40
        ELSE:
            a. SET regular_hours to hours_worked
        
        6. CALCULATE overtime_pay as overtime_hours * (pay_rate * 1.5)
        7. CALCULATE regular_pay as regular_hours * pay_rate
        8. CALCULATE gross_pay as regular_pay + overtime_pay
        
        9. PRINT employee name
        10. PRINT a formatted table with:
            a. Pay Rate
            b. Hours Worked
            c. Overtime Hours
            d. Overtime Pay
            e. Regular Hour Pay
            f. Gross Pay
    END FUNCTION
    """
    
    employee_name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked this week: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    print("-------------------------------------------------")

    overtime_hours = max(0, hours_worked - 40)
    regular_hours = min(hours_worked, 40)

    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    print(f"\nEmployee name: {employee_name}")
    print(f"{'Pay Rate':<10}{'Hours Worked':<15}{'Overtime Hours':<15}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<15}")
    print("--------------------------------------------------------------------------------")
    print(f"{pay_rate:<10.2f}{hours_worked:<15.1f}{overtime_hours:<15.1f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<14.2f}")

calculate_pay()
