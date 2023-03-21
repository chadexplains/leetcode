def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
    memo = {}
    def dfs(i, mask):
        if i == len(workers):
            return 0
        if mask in memo:
            return memo[mask]
        res = float('inf')
        for j in range(len(bikes)):
            if mask & (1 << j) == 0:
                res = min(res, dfs(i + 1, mask | (1 << j)) + self.dist(workers[i], bikes[j]))
        memo[mask] = res
        return res
    return dfs(0, 0)














































































































    def dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])