class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        def dist(p1, p2):
            return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
        def count_in_circle(center):
            count = 0
            for p in points:
                if dist(center, p) <= r:
                    count += 1
            return count
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        n = len(points)
        ans = 1
        for i in range(n):
            for j in range(i+1, n):
                d = dist(points[i], points[j])
                if d > 2*r:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                a = (x1+x2)/2
                b = (y1+y2)/2
                c = (d/2)**0.5
                for k in range(2):
                    center1 = (a + c*(-1)**k, b + c*(-1)**(k^1))
                    count1 = count_in_circle(center1)
                    ans = max(ans, count1)
                    for l in range(k+1, 2):
                        center2 = (a + c*(-1)**l, b + c*(-1)**(l^1))
                        count2 = count_in_circle(center2)
                        ans = max(ans, count2)
                        for m in range(l+1, 2):
                            center3 = (a + c*(-1)**m, b + c*(-1)**(m^1))
                            count3 = count_in_circle(center3)
                            ans = max(ans, count3)
        return ans