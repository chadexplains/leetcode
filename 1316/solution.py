class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        p = 31
        m = 10**9 + 9
        power_mod = [1]
        for i in range(n):
            power_mod.append((power_mod[-1] * p) % m)
        hash_values = [0] * (n + 1)
        for i in range(1, n + 1):
            hash_values[i] = (hash_values[i - 1] + (ord(text[i - 1]) - ord('a') + 1) * power_mod[i - 1]) % m
        distinct_substrings = set()
        for length in range(2, (n // 2) + 1):
            for i in range(n - (2 * length) + 1):
                j = i + length
                k = j + length
                if hash_values[i + length] - hash_values[i] == hash_values[j + length] - hash_values[j] and hash_values[j + length] - hash_values[j] == hash_values[k] - hash_values[j + length]:
                    distinct_substrings.add(text[i:i+length])
        return len(distinct_substrings)