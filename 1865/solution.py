class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        max_ending_here = [arr[0]] * n
        max_starting_here = [arr[-1]] * n
        for i in range(1, n):
            max_ending_here[i] = max(arr[i], max_ending_here[i-1] + arr[i])
        for i in range(n-2, -1, -1):
            max_starting_here[i] = max(arr[i], max_starting_here[i+1] + arr[i])
        max_sum = max(max_ending_here)
        for i in range(1, n-1):
            max_sum = max(max_sum, max_ending_here[i-1] + max_starting_here[i+1])
        for i in range(n):
            if i > 0 and i < n-1:
                max_sum = max(max_sum, max_ending_here[i-1] + max_starting_here[i+1] - arr[i])
        return max_sum