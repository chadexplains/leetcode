class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        n = len(A)
        for i in range(n, 1, -1):
            idx = A.index(i)
            if idx != i - 1:
                if idx != 0:
                    res.append(idx + 1)
                    A[:idx + 1] = reversed(A[:idx + 1])
                res.append(i)
                A[:i] = reversed(A[:i])
        return res