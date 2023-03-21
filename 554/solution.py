class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_freq = {}
        for row in wall:
            prefix_sum = 0
            for brick in row[:-1]:
                prefix_sum += brick
                edge_freq[prefix_sum] = edge_freq.get(prefix_sum, 0) + 1
        return len(wall) - max(edge_freq.values(), default=0)