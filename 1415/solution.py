class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(s):
            if len(s) == n:
                res.append(s)
                return
            for c in ['a', 'b', 'c']:
                if not s or s[-1] != c:
                    backtrack(s + c)
        res = []
        backtrack('')
        return sorted(res)[k-1] if len(res) >= k else ''