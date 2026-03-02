# Delando Grimes
# Date: 03/01/2026
# Assignment: P1HW2 - Travel Expenses
# Description: This program calculates and displays travel expenses
# based on a user-entered budget and estimated costs.

print("This program calculates and displays travel expenses")
print()

# Get user input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate expenses
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

print()
print("------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accommodation: {hotel}")
print(f"Food: {food}")
print()
print(f"Remaining Balance: {remaining_balance}")
