class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        m = len(restrictions)
        for i in range(1, m):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0])
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0])
        ans = 0
        for i in range(1, m):
            h1, id1 = restrictions[i - 1][1], restrictions[i - 1][0]
            h2, id2 = restrictions[i][1], restrictions[i][0]
            d = id2 - id1
            h = (h1 + h2 + d) // 2
            ans = max(ans, h)
        ans = max(ans, restrictions[-1][1] + n - restrictions[-1][0])
        return ans