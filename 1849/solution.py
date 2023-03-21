class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(prev, s):
            if not s:
                return True
            for i in range(1, len(s) + 1):
                curr = int(s[:i])
                if prev is None or prev - curr == 1:
                    if backtrack(curr, s[i:]):
                        return True
            return False
        return backtrack(None, s)