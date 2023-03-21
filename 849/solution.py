class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0
        left_distance = -1
        right_distance = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                left_distance = 0
            else:
                left_distance += 1
            max_distance = max(max_distance, left_distance)
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                right_distance = 0
            else:
                right_distance += 1
            max_distance = max(max_distance, right_distance)
        for i in range(len(seats)):
            if seats[i] == 0:
                left_distance = 0 if i == 0 or seats[i - 1] == 1 else left_distance + 1
                right_distance = 0 if i == len(seats) - 1 or seats[i + 1] == 1 else right_distance + 1
                max_distance = max(max_distance, min(left_distance, right_distance))
        return max_distance