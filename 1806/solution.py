class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left = [0] * n
        right = [0] * n
        count = boxes[0]
        for i in range(1, n):
            left[i] = left[i-1] + count
            count += boxes[i]
        count = boxes[n-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] + count
            count += boxes[i]
        return [left[i] + right[i] for i in range(n)]