class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD
        res = 0
        for i in range(n):
            smaller = 0
            for j in range(i + 1, n):
                if s[j] < s[i]:
                    smaller += 1
            res = (res + smaller * fact[n - i - 1] * inv_fact_counts(s, MOD)[s[i]]) % MOD
        return res

def inv_fact_counts(s, MOD):
    counts = {}
    for c in s:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    inv_fact = {0: 1}
    for i in range(1, len(s) + 1):
        inv_fact[i] = pow(i, MOD - 2, MOD)
    res = {}
    for c, count in counts.items():
        res[c] = inv_fact[count]
    return res