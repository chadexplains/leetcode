class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = '123450'
        start = ''.join(str(num) for row in board for num in row)
        queue = deque([(start, start.index('0'), 0)])
        visited = set([start])
        while queue:
            state, zero_pos, moves = queue.popleft()
            if state == target:
                return moves
            for neighbor in self.get_neighbors(state, zero_pos):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, neighbor.index('0'), moves+1))
        return -1
    def get_neighbors(self, state, zero_pos):
        neighbors = []
        for move in [-1, 1, -3, 3]:
            neighbor_pos = zero_pos + move
            if abs(zero_pos // 3 - neighbor_pos // 3) + abs(zero_pos % 3 - neighbor_pos % 3) == 1 and 0 <= neighbor_pos < 6:
                neighbor = list(state)
                neighbor[zero_pos], neighbor[neighbor_pos] = neighbor[neighbor_pos], neighbor[zero_pos]
                neighbors.append(''.join(neighbor))
        return neighbors