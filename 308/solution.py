class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.bit = [[0] * (n + 1) for _ in range(m + 1)]
        self.matrix = matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.update_bit(i, j, matrix[i - 1][j - 1])

    def update(self, row: int, col: int, val: int) -> None:
        self.update_bit(row + 1, col + 1, val - self.matrix[row][col])
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.get_sum(row2 + 1, col2 + 1) - self.get_sum(row2 + 1, col1) - self.get_sum(row1, col2 + 1) + self.get_sum(row1, col1)

    def update_bit(self, row: int, col: int, val: int) -> None:
        m, n = len(self.bit) - 1, len(self.bit[0]) - 1
        while row <= m:
            while col <= n:
                self.bit[row][col] += val
                col += col & -col
            row += row & -row

    def get_sum(self, row: int, col: int) -> int:
        res = 0
        while row > 0:
            while col > 0:
                res += self.bit[row][col]
                col -= col & -col
            row -= row & -row
        return res
