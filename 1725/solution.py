class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_lengths = [min(rect) for rect in rectangles]
        max_length = max(max_lengths)
        return max_lengths.count(max_length)