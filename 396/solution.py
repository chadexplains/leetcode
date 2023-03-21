class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)
        s = sum(A)
        curr_val = sum(i * A[i] for i in range(n))
        max_val = curr_val
        for k in range(1, n):
            curr_val += s - n * A[n - k]
            max_val = max(max_val, curr_val)
        return max_val