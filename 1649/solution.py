class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10**9 + 7
        n = len(instructions)
        bit = [0] * (max(instructions) + 1)
        def update(x):
            while x <= max(instructions):
                bit[x] += 1
                x += x & -x
        def query(x):
            res = 0
            while x > 0:
                res += bit[x]
                x -= x & -x
            return res
        res = 0
        for i, x in enumerate(instructions):
            less = query(x - 1)
            greater = i - query(x)
            res += min(less, greater)
            update(x)
        return res % mod