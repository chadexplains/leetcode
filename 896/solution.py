class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A[0] <= A[-1]:
            increasing = True
        else:
            increasing = False
        for i in range(1, len(A)):
            if increasing and A[i] < A[i-1]:
                return False
            elif not increasing and A[i] > A[i-1]:
                return False
        return True