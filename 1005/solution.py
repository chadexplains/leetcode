class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        while K > 0 and i < len(A) and A[i] < 0:
            A[i] = -A[i]
            K -= 1
            i += 1
        if K % 2 == 1:
            A.sort()
            A[0] = -A[0]
        return sum(A)