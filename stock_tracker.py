# Task 2: Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 200,
    "AMZN": 300
}

# Welcome message
print("📈 Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Ask user how many stocks they want to enter
num_stocks = int(input("How many different stocks do you want to enter? "))

# Initialize total investment
total_investment = 0

# Create a list to store each stock's summary
stock_summary = []

# Loop to collect stock info
for i in range(num_stocks):
    stock_name = input(f"Enter stock name #{i+1}: ").upper()
    quantity = int(input(f"Enter quantity of {stock_name}: "))

    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment
        summary_line = f"{stock_name}: {quantity} {stock_name} → ₹{price} × {quantity} = ₹{investment}"
        stock_summary.append(summary_line)
        print(summary_line)

    else:
        print(f"{stock_name} is not in our price list.")

# Final result
print("\n💰 Total Investment Value: ₹", total_investment)

# Optional: Save to file
save = input("Do you want to save this result to a file? (yes/no): ").lower()
if save == "yes":
    with open("investment_summary.txt", "w", encoding="utf-8") as file:
        for line in stock_summary:
            file.write(line + "\n")
        file.write(f"\n Total Investment: Rupees {total_investment}\n")
    print("✅ Investment summary saved to 'investment_summary.txt'")
