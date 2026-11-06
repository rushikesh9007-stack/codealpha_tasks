"""
CodeAlpha Python Programming Internship — Task 2: Stock Portfolio Tracker
Calculates the value of a portfolio using example prices defined in a dictionary.
These are sample prices for this programming task, not live market prices.
"""

import csv

STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 165.00,
    "AMZN": 190.00,
}


def get_positive_quantity(stock_name):
    while True:
        raw_value = input(f"Enter quantity of {stock_name}: ").strip()
        try:
            quantity = int(raw_value)
            if quantity <= 0:
                print("Quantity must be a positive whole number.")
                continue
            return quantity
        except ValueError:
            print("Please enter a valid whole number.")


def main():
    portfolio = {}

    print("=" * 42)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 42)
    print("Available stocks and sample prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price:.2f} per share")

    print("\nEnter stock symbols one at a time.")
    print("Type DONE when you have finished.\n")

    while True:
        symbol = input("Stock symbol: ").strip().upper()

        if symbol == "DONE":
            break
        if not symbol:
            print("Please enter a stock symbol.")
            continue
        if symbol not in STOCK_PRICES:
            print("Symbol not found. Choose one from the list above.")
            continue

        quantity = get_positive_quantity(symbol)
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    if not portfolio:
        print("\nNo stocks were entered. Nothing to calculate.")
        return

    print("\nPortfolio Summary")
    print("-" * 42)
    total_investment = 0.0
    rows = []

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total_investment += value
        rows.append([symbol, quantity, f"{price:.2f}", f"{value:.2f}"])
        print(
            f"{symbol}: {quantity} shares × ${price:.2f} = ${value:.2f}"
        )

    print("-" * 42)
    print(f"Total investment value: ${total_investment:.2f}")

    save = input("\nSave summary to portfolio_summary.csv? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio_summary.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock Symbol", "Quantity", "Sample Price (USD)", "Total Value (USD)"])
            writer.writerows(rows)
            writer.writerow(["TOTAL", "", "", f"{total_investment:.2f}"])
        print("Summary saved to portfolio_summary.csv.")


if __name__ == "__main__":
    main()
