# Olijah Dowtin
# October 10, 2026
# P3LAB
# Calculate the fewest dollars and coins needed for an amount of money.

"""
Pseudocode:
1. Ask the user for a money amount.
2. Convert the amount to whole cents.
3. Use floor division to find dollars, then subtract their value.
4. Repeat for quarters, dimes, nickels, and pennies.
5. If the amount is zero, display "No change".
6. Display each denomination only when its count is greater than zero.
7. Use a singular name for one and a plural name for more than one.
"""

money = float(input("Enter the amount of money as a float: $"))
cents = int(round(money * 100))

dollars = cents // 100
cents = cents - dollars * 100

quarters = cents // 25
cents = cents - quarters * 25

dimes = cents // 10
cents = cents - dimes * 10

nickels = cents // 5
cents = cents - nickels * 5

pennies = cents

if money == 0:
    print("No change")

if dollars == 1:
    print("1 Dollar")
elif dollars > 1:
    print(f"{dollars} Dollars")

if quarters == 1:
    print("1 Quarter")
elif quarters > 1:
    print(f"{quarters} Quarters")

if dimes == 1:
    print("1 Dime")
elif dimes > 1:
    print(f"{dimes} Dimes")

if nickels == 1:
    print("1 Nickel")
elif nickels > 1:
    print(f"{nickels} Nickels")

if pennies == 1:
    print("1 Penny")
elif pennies > 1:
    print(f"{pennies} Pennies")
