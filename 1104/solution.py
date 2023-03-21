class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = int(math.log2(label))
        res = []
        while level >= 0:
            res.append(label)
            label = 2 ** (level - 1) + 2 ** level - 1 - label // 2
            level -= 1
        return res[::-1]