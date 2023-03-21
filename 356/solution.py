class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        point_set = set(map(tuple, points))
        x_min = min(point[0] for point in points)
        x_max = max(point[0] for point in points)
        x_sum = x_min + x_max
        for point in points:
            reflected = (x_sum - point[0], point[1])
            if reflected not in point_set:
                return False
        return True