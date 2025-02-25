import requests
import json

class StockPortfolio:
    def __init__(self):
        self.stocks = {}
        self.api_key = "YOUR_API_KEY"  # Replace with a real API key
        self.base_url = "https://financialmodelingprep.com/api/v3/quote/"

    def add_stock(self, symbol, shares, purchase_price):
        self.stocks[symbol] = {
            "shares": shares,
            "purchase_price": purchase_price,
        }

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
        else:
            print("Stock not found in portfolio.")

    def get_stock_price(self, symbol):
        url = f"{self.base_url}{symbol}?apikey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[0]['price']
        return None

    def portfolio_value(self):
        total_value = 0
        for symbol, details in self.stocks.items():
            current_price = self.get_stock_price(symbol)
            if current_price:
                total_value += details['shares'] * current_price
        return total_value

    def display_portfolio(self):
        print("Stock Portfolio:")
        for symbol, details in self.stocks.items():
            current_price = self.get_stock_price(symbol)
            if current_price:
                print(f"{symbol}: {details['shares']} shares, Purchase Price: ${details['purchase_price']}, Current Price: ${current_price}")
        print(f"Total Portfolio Value: ${self.portfolio_value()}")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    portfolio.add_stock("AAPL", 10, 150)
    portfolio.add_stock("GOOGL", 5, 2800)
    portfolio.display_portfolio()
