class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total_pixels = 0
        lines = 1
        for char in s:
            width = widths[ord(char) - ord('a')]
            total_pixels += width
            if total_pixels > 100:
                lines += 1
                total_pixels = width
        return [lines, total_pixels]