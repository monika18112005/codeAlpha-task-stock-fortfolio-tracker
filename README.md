# 🧾 Stock Portfolio Tracker (Python)

This is a simple **command-line stock portfolio tracker** built with Python. It allows users to:

- Enter stock symbols and quantities
- View a summary of their investments
- Save the portfolio summary to a `.txt` or `.csv` file

## 📌 Features

- Hardcoded stock prices for common stocks (e.g., AAPL, TSLA, GOOG)
- Input validation for stock symbols and quantities
- Calculates total investment based on stock prices and user input
- Option to save portfolio data in `.txt` or `.csv` formats

## 🛠️ Technologies Used

- Python 3.x
- No external libraries required

## 🗂️ Stock Prices

The program uses the following predefined prices:

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3300,
    "MSFT": 300
}
