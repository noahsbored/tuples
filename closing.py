def average_closing_price(stock_data, stock_symbol):
    prices = [price for symbol, _, price in stock_data if symbol == stock_symbol]
    return sum(prices) / len(prices) if prices else None


stock_data = [("AAPL", "2021-01-01", 130.0), ("AAPL", "2021-01-02", 132.0), ("MSFT", "2021-01-01", 220.0)]


stock_symbol = "AAPL"
avg_price = average_closing_price(stock_data, stock_symbol)
print(f"Average closing price of {stock_symbol}: {avg_price}" if avg_price else f"No data available for {stock_symbol}")


