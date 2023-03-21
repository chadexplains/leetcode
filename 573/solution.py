class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        total_distance = 0
        max_distance_saved = float('-inf')
        for nut in nuts:
            total_distance += (abs(tree[0] - nut[0]) + abs(tree[1] - nut[1])) * 2
            max_distance_saved = max(max_distance_saved, (abs(squirrel[0] - nut[0]) + abs(squirrel[1] - nut[1])) - (abs(tree[0] - nut[0]) + abs(tree[1] - nut[1])))
        return total_distance - max_distance_saved