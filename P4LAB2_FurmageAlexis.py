#Alexis Furmage
#10-29-24
#P4LAB2
#program that asks the user to enter an integer.

def display_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def main():
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            if user_input < 0:
                print("This program does not handle negative integers.")
            else:
                display_multiplication_table(user_input)

        except ValueError:
            print("Enter a integer: ")

        run_again = input("Would you like to to run the program again? ").strip().lower()
        if run_again != "yes":
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()
