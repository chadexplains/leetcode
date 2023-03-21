class Solution:
    def countHomogenous(self, s: str) -> int:
        count = curr = 1
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i-1]:
                curr += 1
            else:
                count = (count + (curr * (curr + 1)) // 2) % (10**9 + 7)
                curr = 1
        count = (count + (curr * (curr + 1)) // 2) % (10**9 + 7)
        return count