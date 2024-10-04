#Alexis Furmage
#9-28-24
#P2LAB2
#Tests student's knowledge of how to write code that uses a dictionary to store user input and displays output to the user

vehicles_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26}


keys = vehicles_mpg.keys()

print("Available vehicles:", ", ".join(keys))

selected_vehicle = input("Enter a vehicle to see it's mpg:")

if selected_vehicle in vehicles_mpg:
   
    mpg = vehicles_mpg[selected_vehicle]
    print(f"The MPG for the {selected_vehicle} is {mpg}.")
    
    miles = float(input("How many miles will you drive the prius?"))
    
    gallons_needed = miles / mpg
    
    print(f"{gallons_needed:.2f} gallons of gas are needed to drive the prius {miles} miles.")
else:
    print("The vehicle you entered is not in the list. Please try again.")
