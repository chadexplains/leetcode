class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        translations = [(i, j) for i in range(-n+1, n) for j in range(-n+1, n)]
        max_overlap = 0
        for dx, dy in translations:
            overlap = 0
            for i in range(n):
                for j in range(n):
                    if 0 <= i+dx < n and 0 <= j+dy < n and A[i][j] == B[i+dx][j+dy] == 1:
                        overlap += 1
            max_overlap = max(max_overlap, overlap)
        return max_overlap