# Investment Portfolio Tracker

## Project Description
The Investment Portfolio Tracker is a Python-based application that helps users manage and monitor their stock investments.

Users can enter stock ticker symbols, purchase prices, and share quantities. The application retrieves current stock prices using Yahoo Finance and calculates the total investment, current market value, and profit or loss.

The portfolio summary is automatically stored in a CSV file for future reference.

## Features
- Add stock ticker symbols.
- Enter purchase price and share quantity.
- Fetch current stock prices using yfinance.
- Calculate total invested capital.
- Calculate current market value.
- Calculate individual stock profit/loss.
- Calculate overall portfolio performance.
- Export portfolio summaries to CSV.
- Handle invalid inputs and price retrieval errors.

## Technologies Used
- Python 3
- CSV Module
- yfinance
- File Handling
- Dictionary Data Structure

## Installation

Install the required library:

```bash
pip install yfinance
```

## Execution

```bash
python portfolio.py
```

## Output
The application displays a formatted investment portfolio summary in the terminal and automatically generates `portfolio_summary.csv`.

## Author
Aksha Dev A
