# Stock prices dictionary
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200
}

total = 0

print("STOCK PORTFOLIO TRACKER")

# loop for 2 stocks
for i in range(2):

    # user input
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    # check stock exists
    if stock_name in stocks:

        # calculate value
        value = stocks[stock_name] * quantity

        print("Investment Value =", value)

        # add to total
        total = total + value

    else:
        print("Stock not found")

# final total
print("\nTotal Investment Value =", total)