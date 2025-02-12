# Get input from the user
units_consumed = int(input("Enter the number of units consumed: "))

# Calculate the bill
if units_consumed < 50:
    per_unit_cost = 2.60
    tax = 25
elif 50 <= units_consumed < 100:
    per_unit_cost = 3.25
    tax = 35
elif 100 <= units_consumed < 200:
    per_unit_cost = 5.26
    tax = 45
else:  # units_consumed >= 200
    per_unit_cost = 8.45
    tax = 75

# Calculate total bill
total_bill = (units_consumed * per_unit_cost) + tax

# Display the result
print(f"Units Consumed: {units_consumed}")
print(f"Per Unit Cost: {per_unit_cost}")
print(f"Tax: {tax}")
print(f"Total Bill: {total_bill}")
