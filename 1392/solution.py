class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        MOD = 10 ** 9 + 7
        base = 31
        power = 1
        prefix_hash = [0] * (n + 1)
        suffix_hash = [0] * (n + 1)
        for i in range(n):
            prefix_hash[i + 1] = (prefix_hash[i] * base + ord(s[i])) % MOD
            suffix_hash[i + 1] = (suffix_hash[i] + power * ord(s[n - i - 1])) % MOD
            power = (power * base) % MOD
        for i in range(n, 0, -1):
            if prefix_hash[i] == suffix_hash[n - i]:
                return s[:i]
        return ""