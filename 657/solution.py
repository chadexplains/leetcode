class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_count = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
        for move in moves:
            move_count[move] += 1
        return move_count['U'] == move_count['D'] and move_count['L'] == move_count['R']
}