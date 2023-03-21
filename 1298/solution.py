class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        visited = set()
        queue = deque(initialBoxes)
        total_candies = 0
        while queue:
            box = queue.popleft()
            if box not in visited:
                visited.add(box)
                total_candies += candies[box]
                for key in keys[box]:
                    status[key] = 1
                    if key not in visited:
                        queue.append(key)
                for contained_box in containedBoxes[box]:
                    if status[contained_box] == 1:
                        queue.append(contained_box)
                    else:
                        status[contained_box] = -1
        return total_candies