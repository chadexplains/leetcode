def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
    def dfs(i, taken):
        if i == len(workers):
            return 0
        if taken in memo:
            return memo[taken]
        res = float('inf')
        for j in range(len(bikes)):
            if taken & (1 << j) == 0:
                res = min(res, dist(workers[i], bikes[j]) + dfs(i + 1, taken | (1 << j)))
        memo[taken] = res
        return res
    def dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    memo = {}
    return dfs(0, 0)