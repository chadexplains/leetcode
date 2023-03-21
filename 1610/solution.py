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
        i = res = 0
        for j in range(len(angles)):
            while angles[j] - angles[i] > angle:
                i += 1
            res = max(res, j - i + 1)
        return res + same