class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            temp, board[i][j] = board[i][j], '#'
            res = backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1)
            board[i][j] = temp
            return res
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False