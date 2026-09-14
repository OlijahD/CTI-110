# Olijah Dowtin
# September 13, 2026
# P1HW1
# This program performs exponent and addition calculations using intergers entered by the user.

base_value = int(input("Enter an integer as the base value: ")) 
exponent = int(input("Enter an integer as the exponent: "))
result = base_value ** exponent 
print(base_value, "raised to the power of", exponent, "is", result, "!!")
first_number = int(input("Enter the first integer: "))
second_number = int(input("Enter the second integer: "))
third_number = int(input("Enter the third integer: "))
final_result = first_number + second_number - third_number 
print(first_number, "+", second_number, "-", third_number, "is equal to", final_result) 