class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        hold, unhold, cooldown = -prices[0], 0, 0
        for i in range(1, n):
            hold, unhold, cooldown = max(hold, unhold-prices[i]), max(unhold, cooldown), max(cooldown, hold+prices[i])
        return max(unhold, cooldown)