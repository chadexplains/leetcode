class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for row in accounts:
            wealth = sum(row)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth