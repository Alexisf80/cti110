# Your Name
# Date
# P2HW2
# This program calculates and displays the lowest, highest, sum, and average of grades entered by the user.

"""
Pseudocode:
1. Start program
2. Create an empty list named 'grades' to store the grades
3. Prompt the user to enter the grade for Module 1 and store it in the list
4. Prompt the user to enter the grade for Module 2 and store it in the list
5. Prompt the user to enter the grade for Module 3 and store it in the list
6. Prompt the user to enter the grade for Module 4 and store it in the list
7. Prompt the user to enter the grade for Module 5 and store it in the list
8. Prompt the user to enter the grade for Module 6 and store it in the list
9. Calculate the lowest grade using the min() function
10. Calculate the highest grade using the max() function
11. Calculate the sum of grades using the sum() function
12. Calculate the average by dividing the sum of grades by the number of grades
13. Print the results in a formatted manner:
    - Lowest Grade
    - Highest Grade
    - Sum of Grades
    - Average
14. End program
"""

def main():

    module1 = float(input("Enter grade for Module 1: "))
    module2 = float(input("Enter grade for Module 2: "))
    module3 = float(input("Enter grade for Module 3: "))
    module4 = float(input("Enter grade for Module 4: "))
    module5 = float(input("Enter grade for Module 5: "))
    module6 = float(input("Enter grade for Module 6: "))

    grades = [module1, module2, module3, module4, module5, module6]

    lowest_grade = min(grades)
    highest_grade = max(grades)
    sum_of_grades = sum(grades)
    average_grade = sum_of_grades / 6

    print("\n------ Results ------")
    print(f"Lowest Grade: {lowest_grade:.1f}")
    print(f"Highest Grade: {highest_grade:.1f}")
    print(f"Sum of Grades: {sum_of_grades:.1f}")
    print(f"Average: {average_grade:.2f}")
    print("-----------------------")


main()
