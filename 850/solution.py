class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        x_vals = sorted(list(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]])))
        x_i = {v: i for i, v in enumerate(x_vals)}
        lst = [0] * len(x_i)
        prev_y = 0
        area = 0
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, x1, x2, 1))
            events.append((y2, x1, x2, -1))
        events.sort()
        for y, x1, x2, sig in events:
            area += (y - prev_y) * self.query(lst)
            for i in range(x_i[x1], x_i[x2]):
                lst[i] += sig
            prev_y = y
        return area % (10**9 + 7)

    def query(self, lst):
        res = 0
        for i in range(len(lst) - 1):
            if lst[i] > 0:
                res += (lst[i + 1] - lst[i]) * (i + 1)
        return res