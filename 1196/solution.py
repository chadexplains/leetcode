class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        total_weight = 0
        for i in range(len(arr)):
            total_weight += arr[i]
            if total_weight > 5000:
                return i
        return len(arr)