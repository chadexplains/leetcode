class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = {}
        pairs = 0
        for w, h in rectangles:
            ratio = w / h
            if ratio in ratios:
                pairs += ratios[ratio]
                ratios[ratio] += 1
            else:
                ratios[ratio] = 1
        return pairs