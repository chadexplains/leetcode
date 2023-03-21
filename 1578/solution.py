class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        total_cost = max_cost = 0
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i-1]:
                total_cost += min(cost[i], cost[i-1])
                max_cost = max(max_cost, max(cost[i], cost[i-1]))
            else:
                max_cost = 0
        return total_cost - max_cost