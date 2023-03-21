class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        ans = {s}
        if b % 2:
            for i in range(1, n, 2):
                s = s[:i] + str((int(s[i]) + a) % 10) + s[i+1:]
                ans.add(s)
        else:
            s = s[b:] + s[:b]
            ans.add(s)
            for i in range(1, n, 2):
                s = s[:i] + str((int(s[i]) + a) % 10) + s[i+1:]
                ans.add(s[b:] + s[:b])
        return min(ans)