class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq = collections.Counter(nums)
        values = [(freq[num], num) for num in set(nums)]
        values.sort(reverse=True)
        n = len(quantity)
        m = 1 << n
        dp = [False] * m
        dp[0] = True
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if dp[j] and quantity[i] <= sum((j >> k) & 1 for k in range(n) if quantity[k] == quantity[i]):
                    dp[j | (1 << i)] = True
        for j in range(m):
            if dp[j]:
                count = [0] * n
                for k in range(n):
                    if (j >> k) & 1:
                        count[k] = quantity[k]
                if sum(count) == len(nums):
                    return True
        return False