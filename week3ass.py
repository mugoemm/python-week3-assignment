# Function to calculate the final price after applying discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied if less than 20%
        return price


# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"The final price after applying {discount_percent}% discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The price remains: {final_price:.2f}")