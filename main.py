# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 170,
    "AMZN": 190
}

# Store user's portfolio
portfolio = {}

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    # Stop taking input
    if stock == "DONE":
        break

    # Check whether stock exists
    if stock not in stock_prices:
        print("Stock not found. Please choose from:")
        print(", ".join(stock_prices.keys()))
        continue

    # Get quantity
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    # Add stock to portfolio
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
total_investment = 0

print("===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(
        f"{stock}: {quantity} shares × ${price} = ${investment}"
    )

print("------------------------------")
print(f"Total Investment: ${total_investment}")

# Optional: Save results to a text file
save_file = input("\nDo you want to save the result? (yes/no): ").lower()

if save_file == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("===== STOCK PORTFOLIO =====\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity

            file.write(
                f"{stock}: {quantity} shares × ${price} = ${investment}\n"
            )

        file.write("--------------------------\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("Portfolio saved successfully in portfolio.txt")
