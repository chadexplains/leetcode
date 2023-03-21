class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        point_set = set(map(tuple, points))
        min_area = float('inf')
        for p1, p2, p3 in itertools.combinations(points, 3):
            p4 = (p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1])
            if p4 in point_set:
                v21 = complex(p2[0] - p1[0], p2[1] - p1[1])
                v31 = complex(p3[0] - p1[0], p3[1] - p1[1])
                area = abs(v21 * v31)
                if area < min_area:
                    min_area = area
        return min_area if min_area < float('inf') else 0.0