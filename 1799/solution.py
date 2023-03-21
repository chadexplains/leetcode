class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        same = 0
        for x, y in points:
            if x == location[0] and y == location[1]:
                same += 1
                continue
            angles.append(math.atan2(y - location[1], x - location[0]))
        angles.sort()
        angles += [angle + a for a in angles]
        ans = 0
        l = 0
        for r in range(len(angles)):
            while angles[r] - angles[l] > angle:
                l += 1
            ans = max(ans, r - l + 1)
        return ans + same