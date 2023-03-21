def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
    def distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def assign(i, mask):
        if i == len(workers):
            return 0
        if mask in memo:
            return memo[mask]
        ans = float('inf')
        for j in range(len(bikes)):
            if mask & (1 << j) == 0:
                ans = min(ans, distance(workers[i], bikes[j]) + assign(i + 1, mask | (1 << j)))
        memo[mask] = ans
        return ans

    memo = {}
    return assign(0, 0)