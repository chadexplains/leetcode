class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        zeros = 0
        max_len = 0
        for right in range(len(A)):
            if A[right] == 0:
                zeros += 1
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len