class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = collections.deque([('0000', 0)])
        visited = set('0000')
        while queue:
            node, turns = queue.popleft()
            if node == target:
                return turns
            if node in deadends:
                continue
            for i in range(4):
                for j in [-1, 1]:
                    new_node = node[:i] + str((int(node[i]) + j) % 10) + node[i+1:]
                    if new_node not in visited:
                        visited.add(new_node)
                        queue.append((new_node, turns+1))
        return -1