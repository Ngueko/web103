# Input: Allow the user to enter the total for a meal
total = float(input("Enter the total for a meal: "))

# Processing: Calculate tips and totals with tips
tip_15 = total * 0.15
tip_18 = total * 0.18
tip_20 = total * 0.20

total_with_tip_15 = total + tip_15
total_with_tip_18 = total + tip_18
total_with_tip_20 = total + tip_20

# Output: Display total, tip, and total with tip for each tip value
print("\nWith 15% Tip:")
print(f"Total: {total:.2f}")
print(f"Tip: {tip_15:.2f}")
print(f"Total with Tip: {total_with_tip_15:.2f}")

print("\nWith 18% Tip:")
print(f"Total: {total:.2f}")
print(f"Tip: {tip_18:.2f}")
print(f"Total with Tip: {total_with_tip_18:.2f}")

print("\nWith 20% Tip:")
print(f"Total: {total:.2f}")
print(f"Tip: {tip_20:.2f}")
print(f"Total with Tip: {total_with_tip_20:.2f}")