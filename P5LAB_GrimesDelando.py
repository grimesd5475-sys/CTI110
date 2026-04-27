# Delando Grimes
# April 26, 2026
# P5LAB
# Simulates a self-checkout machine and calculates change using a function.

import random

def disperse_change(change):
    change = int(round(change * 100))

    dollars = change // 100
    change %= 100

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    print()

    if dollars > 0:
        print(f"{dollars} Dollars")
    if quarters > 0:
        print(f"{quarters} Quarters")
    if dimes > 0:
        print(f"{dimes} Dimes")
    if nickels > 0:
        print(f"{nickels} Nickels")
    if pennies > 0:
        print(f"{pennies} Pennies")


def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe ${total_owed:.2f}")

    cash = float(input("How much cash will you put in the self-checkout? "))

    change = cash - total_owed

    print(f"Change is: ${change:.2f}")

    if change == 0:
        print("No change")
    else:
        disperse_change(change)


main()
