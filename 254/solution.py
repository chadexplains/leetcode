class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def backtrack(num, start, factors):
            for i in range(start, int(num ** 0.5) + 1):
                if num % i == 0:
                    factors.append(i)
                    backtrack(num // i, i, factors)
                    factors.pop()
                    res.append(factors + [num // i])
            return
        res = []
        backtrack(n, 2, [])
        return res if len(res) > 1 else []
