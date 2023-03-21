class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        dp1, dp2 = [0] * m, [0] * n
        while i < m or j < n:
            if i < m and (j == n or nums1[i] < nums2[j]):
                dp1[i] = max(dp1[i-1] if i > 0 else 0, dp2[j-1] if j > 0 else 0) + nums1[i]
                i += 1
            elif j < n and (i == m or nums1[i] > nums2[j]):
                dp2[j] = max(dp2[j-1] if j > 0 else 0, dp1[i-1] if i > 0 else 0) + nums2[j]
                j += 1
            else:
                dp1[i] = dp2[j] = max(dp1[i-1] if i > 0 else 0, dp2[j-1] if j > 0 else 0) + nums1[i]
                i += 1
                j += 1
        return max(dp1[-1], dp2[-1]) % (10**9 + 7)