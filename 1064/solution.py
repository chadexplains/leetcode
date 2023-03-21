class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == mid:
                return mid
            elif A[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return -1