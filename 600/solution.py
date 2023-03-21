class Solution:
    def findIntegers(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 2
        binary = bin(n)[2:]
        dp = [0] * len(binary)
        dp[0], dp[1] = 1, 2
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        res = dp[-1]
        for i in range(1, len(binary)):
            if binary[i] == '1' and binary[i-1] == '1':
                break
            if binary[i] == '0' and binary[i-1] == '0':
                res -= dp[len(binary)-i-1]
        return res