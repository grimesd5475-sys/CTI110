# Delando Grimes
# 04/12/2026
# P4HW2 - Employee Pay
# This program calculates gross pay for multiple employees,
# including overtime pay, regular pay, and totals for all employees.

# Pseudocode:
# 1. Set totals for overtime pay, regular pay, gross pay, and employee count to 0.
# 2. Ask the user to enter an employee's name or "Done" to stop.
# 3. While the user does not enter "Done":
#    a. Ask for hours worked.
#    b. Ask for pay rate.
#    c. If hours worked is greater than 40:
#       - Calculate overtime hours.
#       - Calculate overtime pay.
#       - Calculate regular pay for 40 hours.
#    d. Otherwise:
#       - Overtime hours and overtime pay are 0.
#       - Calculate regular pay for all hours worked.
#    e. Calculate gross pay.
#    f. Display the employee's pay information.
#    g. Add overtime pay, regular pay, and gross pay to running totals.
#    h. Add 1 to employee count.
#    i. Ask for the next employee's name or "Done" to stop.
# 4. After the loop ends, display:
#    - Total number of employees entered
#    - Total amount paid for overtime
#    - Total amount paid for regular hours
#    - Total amount paid in gross

employee_name = input('Enter employee\'s name or "Done" to terminate: ')

total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

while employee_name != "Done":
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = regular_hours * pay_rate
    else:
        overtime_hours = 0
        regular_hours = hours_worked
        overtime_pay = 0
        regular_pay = regular_hours * pay_rate

    gross_pay = regular_pay + overtime_pay

    print()
    print(f"Employee name:  {employee_name}")
    print()
    print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print("-------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<16.2f}${regular_pay:<14.2f}${gross_pay:.2f}")
    print()

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
