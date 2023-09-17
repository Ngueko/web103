# Input: Allow the user to enter fixed costs, price per unit, and cost per unit
fixed_costs = float(input("Enter the fixed costs: "))
price_per_unit = float(input("Enter the price per unit: "))
cost_per_unit = float(input("Enter the cost per unit: "))

# Processing: Calculate the break-even point
break_even_point = fixed_costs / (price_per_unit - cost_per_unit)

# Output: Display the break-even point
print(f"The break-even point is {break_even_point:.2f} units.")