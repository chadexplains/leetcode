class Solution:
    def numberOfCombinations(self, s: str) -> int:
        n = len(s)
        mod = 10**9 + 7
        primes = set()
        for i in range(2, 100001):
            is_prime = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.add(i)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                if int(s[j:i]) in primes:
                    dp[i] = (dp[i] + dp[j]) % mod
        return dp[n]