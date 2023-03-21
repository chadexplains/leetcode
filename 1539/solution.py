class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
        return arr[left-1] + k - (arr[left-1] - (left-1)) if k > arr[left-1] - (left-1) else arr[left-1] - (arr[left-1] - (left-1) - k)