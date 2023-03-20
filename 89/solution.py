class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            add = 2 ** i
            for j in range(len(res)-1, -1, -1):
                res.append(res[j] + add)
        return res