class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > fee:
                max_profit += price - min_price - fee
                min_price = price - fee
        return max_profit