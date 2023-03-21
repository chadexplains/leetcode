class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        for x, y in dependencies:
            graph[x].append(y)
            indegree[y] += 1
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1, 1 << n):
            available = []
            for i in range(1, n + 1):
                if mask & (1 << (i - 1)):
                    continue
                if indegree[i] == 0:
                    available.append(i)
            if len(available) <= k:
                nxt_mask = mask
                for course in available:
                    nxt_mask |= (1 << (course - 1))
                dp[nxt_mask] = min(dp[nxt_mask], dp[mask] + 1)
            else:
                for comb in combinations(available, k):
                    nxt_mask = mask
                    for course in comb:
                        nxt_mask |= (1 << (course - 1))
                    dp[nxt_mask] = min(dp[nxt_mask], dp[mask] + 1)
        return dp[(1 << n) - 1]