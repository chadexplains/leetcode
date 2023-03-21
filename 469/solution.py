class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        n = len(points)
        prev = 0
        for i in range(n):
            curr = (points[i][0] - points[(i+1)%n][0]) * (points[(i+2)%n][1] - points[(i+1)%n][1]) - (points[i][1] - points[(i+1)%n][1]) * (points[(i+2)%n][0] - points[(i+1)%n][0])
            if curr != 0:
                if curr * prev < 0:
                    return False
                else:
                    prev = curr
        return True