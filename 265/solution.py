class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n, k = len(costs), len(costs[0])
        if k == 1:
            return costs[0][0]
        min1, min2 = float('inf'), float('inf')
        for i in range(n):
            new_min1, new_min2 = float('inf'), float('inf')
            for j in range(k):
                cost = costs[i][j] + (min2 if j == min1 else min1)
                if cost < new_min1:
                    new_min2 = new_min1
                    new_min1 = cost
                elif cost < new_min2:
                    new_min2 = cost
            min1, min2 = new_min1, new_min2
        return min1