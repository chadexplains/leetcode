class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        front_set = set(fronts)
        smallest = float('inf')
        for i, back in enumerate(backs):
            if back not in front_set:
                smallest = min(smallest, back)
        return smallest if smallest != float('inf') else 0