class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        i = 0
        res = 0
        for j in range(m):
            while i < n and nums1[i] > nums2[j]:
                i += 1
            if i == n:
                break
            res = max(res, j - i)
        return res