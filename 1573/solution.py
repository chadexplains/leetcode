class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        ones = [0] * n
        ones[0] = int(s[0])
        for i in range(1, n):
            ones[i] = ones[i - 1] + int(s[i])
        if ones[-1] % 3 != 0:
            return 0
        if ones[-1] == 0:
            return (n - 1) * (n - 2) // 2 % MOD
        target = ones[-1] // 3
        first, second = [], []
        for i in range(n - 2):
            if ones[i] == target:
                first.append(i)
            if ones[i] == 2 * target:
                second.append(i)
        ans = 0
        j = 0
        for i in first:
            while j < len(second) and second[j] <= i:
                j += 1
            ans += len(second) - j
        return ans % MOD