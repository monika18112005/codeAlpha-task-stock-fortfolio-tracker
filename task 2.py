# Define hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3300,
    "MSFT": 300
}

# Initialize portfolio dictionary
portfolio = {}

# Function to get user input
def get_user_input():
    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").upper()
        if symbol == 'DONE':
            break
        if symbol not in stock_prices:
            print(f"Stock symbol '{symbol}' not found in price list.")
            continue
        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                continue
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print("Invalid quantity. Please enter a number.")

# Function to calculate total investment
def calculate_total_investment():
    total = 0
    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        total += price * quantity
    return total

# Function to display portfolio
def display_portfolio():
    print("\nYour Portfolio:")
    print("{:<10} {:<10} {:<10}".format("Symbol", "Quantity", "Price"))
    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        print("{:<10} {:<10} ${:<10}".format(symbol, quantity, price))
    total = calculate_total_investment()
    print(f"\nTotal Investment: ${total}")

# Function to save portfolio to file
def save_to_file(filename, filetype='txt'):
    try:
        with open(f"{filename}.{filetype}", 'w') as file:
            if filetype == 'csv':
                file.write("Symbol,Quantity,Price\n")
                for symbol, quantity in portfolio.items():
                    price = stock_prices[symbol]
                    file.write(f"{symbol},{quantity},{price}\n")
                file.write(f"Total Investment,,{calculate_total_investment()}\n")
            else:
                file.write("Your Portfolio:\n")
                for symbol, quantity in portfolio.items():
                    price = stock_prices[symbol]
                    file.write(f"{symbol}: Quantity={quantity}, Price=${price}\n")
                file.write(f"\nTotal Investment: ${calculate_total_investment()}\n")
        print(f"Portfolio saved to {filename}.{filetype}")
    except Exception as e:
        print(f"Error saving file: {e}")

# Main program
def main():
    get_user_input()
    if not portfolio:
        print("No stocks entered.")
        return
    display_portfolio()
    save = input("Would you like to save the portfolio to a file? (yes/no): ").lower()
    if save == 'yes':
        filename = input("Enter filename (without extension): ")
        filetype = input("Enter file type ('txt' or 'csv'): ").lower()
        if filetype not in ['txt', 'csv']:
            print("Invalid file type. Defaulting to 'txt'.")
            filetype = 'txt'
        save_to_file(filename, filetype)

if __name__ == "__main__":
    main()
