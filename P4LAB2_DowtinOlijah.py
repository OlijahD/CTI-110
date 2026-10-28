# Olijah Dowtin
# October 27, 2026
# P4LAB2
# Use loops to display a multiplication table and repeat the program.

# Pseudocode:
# 1. Set run_again to "yes" so the program runs at least once.
# 2. Display the student's name and assignment name.
# 3. While run_again is "yes":
#    a. Ask the user to enter an integer and convert the input to int.
#    b. If the integer is zero or positive:
#       Use a for loop with multipliers 1 through 12.
#       Multiply the integer by each multiplier and display the equation.
#    c. Otherwise, display that negative values are not accepted.
#    d. Ask whether the user wants to run again (yes or no).
#       Remove extra spaces and convert the response to lowercase.
# 4. Repeat when the answer is "yes"; exit when the answer is "no".
# 5. Display a goodbye message after the loop ends.

print("Olijah Dowtin - P4LAB2")
run_again = "yes"

while run_again == "yes":
    number = int(input("\nEnter an integer: "))

    if number >= 0:
        for multiplier in range(1, 13):
            print(f"{number} * {multiplier} = {number * multiplier}")
    else:
        print("Negative values are not accepted.")

    run_again = input("\nWould you like to run the program again? (yes/no): ").strip().lower()

print("\nExiting program. Goodbye!")
