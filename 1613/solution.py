class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x1 = x2 = y1 = y2 = 0
        for i in range(len(s1)):
            if s1[i] == 'x':
                x1 += 1
            else:
                y1 += 1
            if s2[i] == 'x':
                x2 += 1
            else:
                y2 += 1
        if x1 != x2 or y1 != y2:
            return -1
        xy = yx = 0
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                xy += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                yx += 1
        return (xy + 1) // 2 + (yx + 1) // 2