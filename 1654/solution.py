class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0:
            return 0
        forbidden_set = set(forbidden)
        max_pos = max(forbidden + [x])
        queue = deque([(0, 0)])
        visited = set([(0, False)])
        while queue:
            pos, jumps = queue.popleft()
            if pos == x:
                return jumps
            forward_pos = pos + a
            if forward_pos <= max_pos and forward_pos not in forbidden_set and (forward_pos, True) not in visited:
                visited.add((forward_pos, True))
                queue.append((forward_pos, jumps + 1))
            backward_pos = pos - b
            if backward_pos > 0 and backward_pos not in forbidden_set and (backward_pos, False) not in visited:
                visited.add((backward_pos, False))
                queue.append((backward_pos, jumps + 1))
        return -1