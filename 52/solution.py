class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diagonals, anti_diagonals):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                diagonal = row - col
                anti_diagonal = row + col
                if col in cols or diagonal in diagonals or anti_diagonal in anti_diagonals:
                    continue
                cols.add(col)
                diagonals.add(diagonal)
                anti_diagonals.add(anti_diagonal)
                backtrack(row + 1, cols, diagonals, anti_diagonals)
                cols.remove(col)
                diagonals.remove(diagonal)
                anti_diagonals.remove(anti_diagonal)
        count = 0
        backtrack(0, set(), set(), set())
        return count