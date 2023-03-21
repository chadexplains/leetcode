class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closest_x = max(x1, min(x_center, x2))
        closest_y = max(y1, min(y_center, y2))
        distance = ((closest_x - x_center) ** 2 + (closest_y - y_center) ** 2) ** 0.5
        return distance <= radius