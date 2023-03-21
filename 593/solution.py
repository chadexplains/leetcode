class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        distances = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5
                distances.append(distance)
        distances.sort()
        if distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]:
            return True
        elif distances[0] == distances[1] == distances[2] and distances[3] == distances[4] == distances[5]:
            return True
        else:
            return False