class Solution:
    def longestMountain(self, A: List[int]) -> int:
        start, peak, end = 0, -1, 0
        max_length = 0
        while end < len(A) - 1:
            if start == end:
                if A[start] >= A[start + 1]:
                    start += 1
                else:
                    peak = start + 1
                    end = peak
            elif A[end] > A[end + 1]:
                if peak != -1:
                    max_length = max(max_length, end - start + 1)
                if A[end] > A[peak]:
                    peak = end
                end += 1
            elif A[end] < A[end + 1]:
                end += 1
                if peak == -1:
                    start = end
            else:
                if peak != -1:
                    max_length = max(max_length, end - start + 1)
                start = end
                peak = -1
        if peak != -1:
            max_length = max(max_length, end - start + 1)
        return max_length