def maxProfit(prices):
    n = len(prices)
    if n == 0:
        return 0
    left = [0] * n
    right = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left[i] = max(left[i-1], prices[i] - min_price)
    max_price = prices[n-1]
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        right[i] = max(right[i+1], max_price - prices[i])
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, left[i] + right[i])
    return max_profit