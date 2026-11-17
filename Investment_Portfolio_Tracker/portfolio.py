import csv
import os
from datetime import datetime

# Import yfinance for live stock prices
try:
    import yfinance as yf
except ImportError:
    yf = None


# Dictionary to store portfolio details
portfolio = {}


# Function to get positive decimal input
def get_positive_float(message):
    while True:
        try:
            value = float(input(message))

            if value <= 0:
                print("Please enter a value greater than zero.")
            else:
                return value

        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Function to get positive integer input
def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value <= 0:
                print("Please enter a quantity greater than zero.")
            else:
                return value

        except ValueError:
            print("Invalid input! Please enter a valid integer.")


# Function to fetch current stock price
def get_current_price(ticker):
    if yf is None:
        print("\nyfinance is not installed.")
        return None

    try:
        stock = yf.Ticker(ticker)

        # Try getting the latest available price
        price = stock.fast_info.get("last_price")

        if price is not None and price > 0:
            return float(price)

        # Alternative method using historical data
        history = stock.history(period="5d")

        if not history.empty:
            price = history["Close"].dropna()

            if not price.empty:
                return float(price.iloc[-1])

    except Exception as error:
        print(f"Could not fetch price for {ticker}: {error}")

    return None


# Function to add stocks to portfolio
def add_stock():

    print("\n--- ADD STOCK TO PORTFOLIO ---")

    while True:
        ticker = input("\nEnter stock ticker symbol (or DONE): ").strip().upper()

        if ticker == "DONE":
            break

        if not ticker:
            print("Ticker symbol cannot be empty.")
            continue

        if ticker in portfolio:
            print("This stock is already in your portfolio.")
            continue

        buy_price = get_positive_float("Enter purchase price per share: ")

        quantity = get_positive_integer("Enter number of shares: ")

        portfolio[ticker] = {
            "buy_price": buy_price,
            "quantity": quantity
        }

        print(f"\n{ticker} added successfully!")


# Function to calculate portfolio performance
def calculate_portfolio():

    total_investment = 0
    total_market_value = 0
    results = []

    print("\nFetching current stock prices...")

    for ticker, details in portfolio.items():

        buy_price = details["buy_price"]
        quantity = details["quantity"]

        current_price = get_current_price(ticker)

        # Manual price entry if live price is unavailable
        if current_price is None:
            print(f"\nUnable to retrieve live price for {ticker}.")
            current_price = get_positive_float(
                f"Enter current price for {ticker}: "
            )

        invested_amount = buy_price * quantity
        market_value = current_price * quantity

        profit_loss = market_value - invested_amount

        if invested_amount > 0:
            percentage = (profit_loss / invested_amount) * 100
        else:
            percentage = 0

        total_investment += invested_amount
        total_market_value += market_value

        results.append({
            "ticker": ticker,
            "quantity": quantity,
            "buy_price": buy_price,
            "current_price": current_price,
            "invested_amount": invested_amount,
            "market_value": market_value,
            "profit_loss": profit_loss,
            "percentage": percentage
        })

    total_profit_loss = total_market_value - total_investment

    if total_investment > 0:
        total_percentage = (
            total_profit_loss / total_investment
        ) * 100
    else:
        total_percentage = 0

    return (
        results,
        total_investment,
        total_market_value,
        total_profit_loss,
        total_percentage
    )


# Function to display portfolio summary
def display_portfolio(results, investment, market_value, profit_loss, percentage):

    print("\n")
    print("=" * 105)
    print("                 INVESTMENT PORTFOLIO SUMMARY")
    print("=" * 105)

    print(
        f"{'TICKER':<12}"
        f"{'QUANTITY':<12}"
        f"{'BUY PRICE':<14}"
        f"{'CURRENT PRICE':<17}"
        f"{'INVESTED':<14}"
        f"{'MARKET VALUE':<16}"
        f"{'GAIN/LOSS %':<12}"
    )

    print("-" * 105)

    for stock in results:

        print(
            f"{stock['ticker']:<12}"
            f"{stock['quantity']:<12}"
            f"{stock['buy_price']:<14.2f}"
            f"{stock['current_price']:<17.2f}"
            f"{stock['invested_amount']:<14.2f}"
            f"{stock['market_value']:<16.2f}"
            f"{stock['percentage']:<12.2f}"
        )

    print("-" * 105)

    print(f"\nTotal Invested Capital : {investment:.2f}")
    print(f"Total Market Value     : {market_value:.2f}")
    print(f"Total Profit / Loss    : {profit_loss:.2f}")
    print(f"Overall Gain / Loss    : {percentage:.2f}%")

    if profit_loss > 0:
        print("\nPortfolio Status: PROFIT")
    elif profit_loss < 0:
        print("\nPortfolio Status: LOSS")
    else:
        print("\nPortfolio Status: NO PROFIT OR LOSS")

    print("=" * 105)


# Function to save summary into CSV file
def save_to_csv(results, investment, market_value, profit_loss, percentage):

    filename = "portfolio_summary.csv"

    file_exists = os.path.isfile(filename) and os.path.getsize(filename) > 0

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    fieldnames = [
        "Date and Time",
        "Type",
        "Ticker",
        "Quantity",
        "Buy Price",
        "Current Price",
        "Invested Amount",
        "Market Value",
        "Profit/Loss",
        "Gain/Loss Percentage"
    ]

    try:
        with open(filename, "a", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            # Save individual stock details
            for stock in results:

                writer.writerow({
                    "Date and Time": timestamp,
                    "Type": "Stock",
                    "Ticker": stock["ticker"],
                    "Quantity": stock["quantity"],
                    "Buy Price": round(stock["buy_price"], 2),
                    "Current Price": round(stock["current_price"], 2),
                    "Invested Amount": round(stock["invested_amount"], 2),
                    "Market Value": round(stock["market_value"], 2),
                    "Profit/Loss": round(stock["profit_loss"], 2),
                    "Gain/Loss Percentage": round(stock["percentage"], 2)
                })

            # Save overall portfolio details
            writer.writerow({
                "Date and Time": timestamp,
                "Type": "Portfolio Total",
                "Ticker": "ALL",
                "Quantity": "",
                "Buy Price": "",
                "Current Price": "",
                "Invested Amount": round(investment, 2),
                "Market Value": round(market_value, 2),
                "Profit/Loss": round(profit_loss, 2),
                "Gain/Loss Percentage": round(percentage, 2)
            })

        print(f"\nPortfolio summary saved successfully to {filename}")

    except OSError as error:
        print(f"\nError saving CSV file: {error}")


# Main function
def main():

    print("\n" + "=" * 55)
    print("          INVESTMENT PORTFOLIO TRACKER")
    print("=" * 55)

    print("\nWelcome to the Investment Portfolio Tracker!")

    add_stock()

    if not portfolio:
        print("\nNo stocks were added. Exiting program.")
        return

    (
        results,
        investment,
        market_value,
        profit_loss,
        percentage
    ) = calculate_portfolio()

    display_portfolio(
        results,
        investment,
        market_value,
        profit_loss,
        percentage
    )

    save_to_csv(
        results,
        investment,
        market_value,
        profit_loss,
        percentage
    )

    print("\nThank you for using Investment Portfolio Tracker!")


# Program execution
if __name__ == "__main__":
    main()