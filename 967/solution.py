class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        def backtrack(num):
            if len(num) == N:
                res.append(int(num))
                return
            for i in range(10):
                if i == 0 and not num:
                    continue
                if num and abs(int(num[-1]) - i) == K:
                    backtrack(num + str(i))
        res = []
        if N == 1:
            res.append(0)
        for i in range(1, 10):
            backtrack(str(i))
        return res