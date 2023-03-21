class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ['' for _ in range(numRows)]
        curr_row = 0
        direction = -1
        for c in s:
            rows[curr_row] += c
            if curr_row == 0 or curr_row == numRows - 1:
                direction *= -1
            curr_row += direction
        return ''.join(rows)