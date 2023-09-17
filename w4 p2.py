# Input: Allow the user to enter the purchase price per share, current stock price, and quantity of stock
purchase_price_per_share = float(input("Enter the purchase price per share: "))
current_stock_price = float(input("Enter the current stock price: "))
quantity_of_stock = int(input("Enter the quantity of stock: "))

# Processing: Calculate the increase (or decrease) in the value of the stock
value = (current_stock_price - purchase_price_per_share) * quantity_of_stock

# Output: Display the increase (or decrease) in the value of the stock
if value > 0:
    print(f"The value of your stock has increased by ${value:.2f}")
elif value < 0:
    print(f"You are losing money. The value of your stock has decreased by ${abs(value):.2f}")
else:
    print("The value of your stock has remained the same.")