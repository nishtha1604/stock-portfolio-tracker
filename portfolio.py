stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        portfolio[stock_name] = quantity
    else:
        print("Stock not available.")

print("\nPortfolio Summary")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock} -> Quantity: {quantity}, Total: ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

with open("portfolio_summary.txt", "w") as file:
    file.write("Portfolio Summary\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(f"{stock} -> Quantity: {quantity}, Total: ${investment}\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nFile saved successfully!")