class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        num = 1
        direction = 'right'
        row, col = 0, 0
        while num <= n * n:
            matrix[row][col] = num
            num += 1
            if direction == 'right':
                if col == n - 1 or matrix[row][col + 1] != 0:
                    direction = 'down'
                    row += 1
                else:
                    col += 1
            elif direction == 'down':
                if row == n - 1 or matrix[row + 1][col] != 0:
                    direction = 'left'
                    col -= 1
                else:
                    row += 1
            elif direction == 'left':
                if col == 0 or matrix[row][col - 1] != 0:
                    direction = 'up'
                    row -= 1
                else:
                    col -= 1
            elif direction == 'up':
                if row == 0 or matrix[row - 1][col] != 0:
                    direction = 'right'
                    col += 1
                else:
                    row -= 1
        return matrix