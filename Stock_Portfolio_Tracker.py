stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 300
}

print("Available stocks:", ", ".join(stocks.keys()))
stock_name = input("Enter stock name: ").upper().strip()
if stock_name not in stocks:
    print("Error: stock not found. Available:", ", ".join(stocks.keys()))
    raise SystemExit(1)

try:
    quantity = int(input("Enter quantity: "))
    if quantity <= 0:
        raise ValueError()
except ValueError:
    print("Error: quantity must be a positive integer")
    raise SystemExit(1)

total = stocks[stock_name] * quantity
with open("portfolio.txt", "a") as file:
    file.write(f"{stock_name} x{quantity} @ {stocks[stock_name]} = Total Investment: {total}\n")

print(f"Saved: {stock_name} x{quantity} -> Total Investment: {total}")