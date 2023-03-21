class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        coords = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                coords[board[i][j]] = (i, j)
        curr_pos = (0, 0)
        ans = ""
        for c in target:
            target_pos = coords[c]
            dist = (target_pos[0] - curr_pos[0], target_pos[1] - curr_pos[1])
            if dist[0] > 0:
                ans += 'D' * dist[0]
            if dist[1] > 0:
                ans += 'R' * dist[1]
            if dist[0] < 0:
                ans += 'U' * (-dist[0])
            if dist[1] < 0:
                ans += 'L' * (-dist[1])
            ans += '!' # add character at target position
            curr_pos = target_pos
        return ans