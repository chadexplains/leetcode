class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        n = len(arr)
        for i in range(n):
            contribution = ((i + 1) * (n - i) + 1) // 2
            result += contribution * arr[i]
        return result