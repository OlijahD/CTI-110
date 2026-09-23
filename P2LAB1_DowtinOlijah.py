# Olijah Dowtin
# September 23, 2026
# P2LAB1
# Calculate and display a circle's diameter, circumference, and area.

# Pseudocode:
# Ask the user for the radius as a decimal number.
# Calculate the diameter, circumference, and area.
# Display each result with the required decimal places.

import math

radius = float(input("Enter the radius of the circle: "))
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")