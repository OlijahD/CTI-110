# Olijah Dowtin
# September 23, 2026
# P2LAB2
# This program uses a dictionary to find a vehicle's MPG
# and calculate how many gallons of gas a trip needs.

# Create a dictionary with vehicle names and their MPG.
# Show the available vehicles.
# Ask the user to choose a vehicle and show its MPG.
# Ask how many miles the user will drive.
# Divide miles by MPG to find gallons needed.
# Display the gallons rounded to two decimal places.

cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = cars.keys()
print(keys)

vehicle = input("Enter a vehicle exactly as shown above: ")
mpg = cars[vehicle]
print(f"The {vehicle} gets {mpg} MPG.")
miles = float(input("How many miles will you drive? "))
gallons = miles / mpg
print(f"Gallons of gas needed: {gallons:.2f}")