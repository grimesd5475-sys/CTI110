# Delando Grimes
# 03/22/2026
# P3LAB
# This program takes a money amount and calculates the most efficient
# number of dollars, quarters, dimes, nickels, and pennies.

# Get user input
amount = float(input("Enter the amount of money as a float: $"))

# Convert to cents
total_cents = int(amount * 100)

# If no money entered
if total_cents == 0:
    print("No change")
else:
    # Calculate values
    dollars = total_cents // 100
    total_cents -= dollars * 100

    quarters = total_cents // 25
    total_cents -= quarters * 25

    dimes = total_cents // 10
    total_cents -= dimes * 10

    nickels = total_cents // 5
    total_cents -= nickels * 5

    pennies = total_cents

    # Output
    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(dollars, "Dollars")

    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(quarters, "Quarters")

    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(dimes, "Dimes")

    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(nickels, "Nickels")

    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(pennies, "Pennies")