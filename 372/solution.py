class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        phi = 1140
        res = 1
        for i in range(len(b)):
            res = pow(res, 10, 1337) * pow(a, b[i], 1337) % 1337
        return res