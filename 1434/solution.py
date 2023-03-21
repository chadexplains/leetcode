class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        MOD = 10**9 + 7
        hat_to_person = [set() for _ in range(41)]
        for i in range(n):
            for hat in hats[i]:
                hat_to_person[hat].add(i)
        dp = [0] * (1 << n)
        dp[0] = 1
        for hat in range(1, 41):
            for i in range((1 << n) - 1, -1, -1):
                for person in hat_to_person[hat]:
                    if i & (1 << person):
                        dp[i] = (dp[i] + dp[i - (1 << person)]) % MOD
        return dp[(1 << n) - 1]