class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        a = b = 0
        res = []
        for c in seq:
            if c == '(':  # assign to group with lower current nesting depth
                if a < b:
                    a += 1
                    res.append(0)
                else:
                    b += 1
                    res.append(1)
            else:  # assign to group with higher current nesting depth
                if a > b:
                    a -= 1
                    res.append(0)
                else:
                    b -= 1
                    res.append(1)
        return res
