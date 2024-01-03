# Data
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate the total price average for all products
total_price_average = sum(prices) / len(prices)
print(f"Total Price Average: ${total_price_average:.2f}")

# Create a new price list that reduces the old prices by $5
new_price = []
for i in range(0, len(prices)):
    new_price.append( prices[i] - 5)
print("New Prices: ", new_price)
#new_prices = [price - 5 for price in prices]
#print(f"New Prices: {new_prices}")

# Calculate the total revenue generated from the products
sales = []
for i in range(0, len(prices)):
    sales.append(prices[i] * last_week[i])
 
# printing resultant list 
print ("Sale : " + str(sales))
print("Total Revenue: $", sum(sales))
#total_revenue = sum([price * quantity for price, quantity in zip(prices, last_week)])
#print(f"Total Revenue: ${total_revenue:.2f}")

# Calculate the average daily revenue generated from the products
average_daily_revenue = sum(sales) / sum(last_week)
print(f"Average Daily Revenue: ${average_daily_revenue:.2f}")

# Products less than $30 based on the new prices
less_prod = []
for i in range(0, len(new_price)):
    if new_price[i] < 30:
        less_prod.append(products[i])

#less_than_30_products = [product for product, price in zip(products, new_price) if price < 30]
print(f"Products Less Than $30:", less_prod)
