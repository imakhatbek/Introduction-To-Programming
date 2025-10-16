#test
print("Hello world!") 
print(2+2)
print(2*4) 
print(9/3)

#example 1 

bitcoin_price = 55000
bitcoin_amount = 0.754
portfolio_value = bitcoin_price * bitcoin_amount
print("Current Bitcoin price: $", round(bitcoin_price, 2))  
print("Your Bitcoin holdings:", round(bitcoin_amount, 5), "BTC")  
print("Portfolio value: $", round(portfolio_value, 3))

#example 2
item_price = 25.50
quantity = 3
tax_rate = 0.08
subtotal = item_price * quantity
tax = subtotal * tax_rate
total_cost = subtotal + tax

print("Price per item: $", round(item_price, 2))
print("Quantity:", quantity)
print("Subtotal: $", round(subtotal, 2))
print("Tax (8%): $", round(tax, 2))
print("Total cost: $", round(total_cost, 2))
