class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        overlap_width = min(C, G) - max(A, E)
        overlap_height = min(D, H) - max(B, F)
        overlap_area = max(overlap_width, 0) * max(overlap_height, 0)
        return area1 + area2 - overlap_area