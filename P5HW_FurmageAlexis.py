#Alexis Furmage
#11/18/24
#P5HW
#Use of loops, functions and module import to complete a program

import random

def addition_quiz():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    correct_answer = num1 + num2
    print("\n", num1, "\n+ ", num2, sep="")
    guesses = 0

    while True:
        user_answer = int(input("\nEnter answer.\n"))
        guesses += 1
        if user_answer == correct_answer:
            print("Congratulations!!!! Your answer is correct.\nNumber of guesses:", guesses, "\n")
            break
        elif user_answer < correct_answer:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

def subtraction_quiz():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    correct_answer = num1 - num2
    print("\n", num1, "\n- ", num2, sep="")
    guesses = 0

    while True:
        user_answer = int(input("\nEnter answer.\n"))
        guesses += 1
        if user_answer == correct_answer:
            print("Congratulations!!!! Your answer is correct.\nNumber of guesses:", guesses, "\n")
            break
        elif user_answer < correct_answer:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

def main_menu():
    while True:
        print("Welcome to Math Quiz")
        print("\nMAIN MENU")
        print("--------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        
        choice = int(input("\nPlease choose one of the menu options: "))
        if choice == 1:
            addition_quiz()
        elif choice == 2:
            subtraction_quiz()
        elif choice == 3:
            print("Thank you for playing... Bye!!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")

main_menu()



