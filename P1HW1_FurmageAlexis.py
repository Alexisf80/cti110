#Alexis Furmage
#09-19-24
#P1HW1
##Writing code that collects info from user,processes information collected and display results to user.
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base ** exponent

print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

starting_integer = int(input("Enter a starting integer: "))
add_integer = int(input("Enter an integer to add: "))
subtract_integer = int(input("Enter an integer to subtract: "))

total = starting_integer + add_integer - subtract_integer

print(f"\n{starting_integer} + {add_integer} - {subtract_integer} is equal to {total}")
