class Solution:
    def minimumBoxes(self, n: int) -> int:
        k = int((-1 + (1 + 8 * n) ** 0.5) / 2)
        total_boxes = k * (k + 1) // 2
        return total_boxes - n if total_boxes >= n else k + 1