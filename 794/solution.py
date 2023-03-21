class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)
        if o_count not in {x_count-1, x_count}:
            return False
        if self.wins(board, 'X') and x_count-1 != o_count:
            return False
        if self.wins(board, 'O') and x_count != o_count:
            return False
        return True

    def wins(self, board, player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
            if all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2-i] == player for i in range(3)):
            return True
        return False