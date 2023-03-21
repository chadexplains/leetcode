class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[-1] * (fuel + 1) for _ in range(n)]
        mod = 10 ** 9 + 7
        def dfs(city, cur_fuel):
            if cur_fuel < 0:
                return 0
            if dp[city][cur_fuel] != -1:
                return dp[city][cur_fuel]
            if city == finish:
                return 1
            res = 0
            for i in range(n):
                if i != city:
                    res += dfs(i, cur_fuel - abs(locations[city] - locations[i]))
            dp[city][cur_fuel] = res % mod
            return dp[city][cur_fuel]
        return dfs(start, fuel)