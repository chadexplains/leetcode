class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n
        max_count = 0
        for i in range(n):
            slopes = defaultdict(int)
            same_points = 1
            for j in range(i+1, n):
                if points[i] == points[j]:
                    same_points += 1
                else:
                    dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                    gcd = math.gcd(dx, dy)
                    slope = (dx // gcd, dy // gcd)
                    slopes[slope] += 1
            if not slopes:
                max_count = max(max_count, same_points)
            else:
                max_count = max(max_count, same_points + max(slopes.values()))
        return max_count