class Solution:
    def search(self, reader, target):
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1
        while left <= right:
            mid = (left + right) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1