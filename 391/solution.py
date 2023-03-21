class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        area = 0
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            area += (x2 - x1) * (y2 - y1)
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        if len(corners) != 4:
            return False
        corners = sorted(corners)
        return area == (corners[-1][0] - corners[0][0]) * (corners[-1][1] - corners[0][1]) and \
               (corners[0], corners[1], corners[2], corners[3]) == tuple(rectangles)