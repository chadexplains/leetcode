class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        def dfs(i, total):
            if abs(total - target) < abs(self.ans - target) or abs(total - target) == abs(self.ans - target) and total < self.ans:
                self.ans = total
            if i == len(toppingCosts) or total >= target:
                return
            dfs(i + 1, total)
            dfs(i + 1, total + toppingCosts[i])
            dfs(i + 1, total + 2 * toppingCosts[i])
        self.ans = baseCosts[0]
        for base in baseCosts:
            dfs(0, base)
        return self.ans