class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val, max_val = arrays[0][0], arrays[0][-1]
        min_idx, max_idx = 0, 0
        max_distance = 0
        for i in range(1, len(arrays)):
            curr_min, curr_max = arrays[i][0], arrays[i][-1]
            curr_distance = max(abs(curr_max - min_val), abs(max_val - curr_min))
            max_distance = max(max_distance, curr_distance)
            if curr_min < min_val:
                min_val = curr_min
                min_idx = i
            if curr_max > max_val:
                max_val = curr_max
                max_idx = i
        return max_distance