class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [[""] * len(s) for _ in range(numRows)]
        row, col, direction = 0, 0, 1
        for char in s:
            res[row][col] = char
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            row += direction
            col += 1
        return "".join([res[i][j] for j in range(len(s)) for i in range(numRows) if res[i][j]])
