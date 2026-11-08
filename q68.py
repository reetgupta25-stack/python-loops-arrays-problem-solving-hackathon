prices = [7, 1, 5, 3, 6, 4]
min_price = float("inf")
best_profit = 0
for price in prices:
    min_price = min(min_price, price)
    best_profit = max(best_profit, price - min_price)
print(best_profit)