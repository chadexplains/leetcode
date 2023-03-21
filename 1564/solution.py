def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        n = len(warehouse)
        min_height = [0] * n
        min_height[0] = warehouse[0]
        for i in range(1, n):
            min_height[i] = min(min_height[i-1], warehouse[i])
        i, j = 0, 0
        while i < len(boxes) and j < n:
            if boxes[i] <= min_height[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i