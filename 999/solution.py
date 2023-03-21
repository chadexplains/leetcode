class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x, y = i, j
        count = 0
        for i, j in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            dx, dy = x + i, y + j
            while 0 <= dx < 8 and 0 <= dy < 8:
                if board[dx][dy] == 'B':
                    break
                if board[dx][dy] == 'p':
                    count += 1
                    break
                dx += i
                dy += j
        return count