class Solution:
    def countDistinct(self, s: str) -> int:
        n = len(s)
        sa = [i for i in range(n)]
        sa.sort(key=lambda i: s[i:])
        lcp = [0] * n
        for i in range(1, n):
            j = sa[i - 1]
            while i + lcp[i - 1] < n and j + lcp[i - 1] < n and s[i + lcp[i - 1]] == s[j + lcp[i - 1]]:
                lcp[i - 1] += 1
            lcp[i] = lcp[i - 1] - 1 if lcp[i - 1] > 0 else 0
        return sum(n - i for i in sa) - sum(lcp)