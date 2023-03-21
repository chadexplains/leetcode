class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        for c in range(len(A[0])):
            if any(A[i][c] > A[i+1][c] for i in range(len(A)-1)):
                count += 1
        return count