class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sorted_nums1 = sorted(nums1)
        max_diff = 0
        total_diff = 0
        for i in range(len(nums2)):
            diff = abs(nums1[i] - nums2[i])
            total_diff += diff
            j = bisect_left(sorted_nums1, nums2[i])
            if j < len(nums1):
                max_diff = max(max_diff, diff - (sorted_nums1[j] - nums2[i]))
            if j > 0:
                max_diff = max(max_diff, diff - (nums2[i] - sorted_nums1[j-1]))
        return (total_diff - max_diff) % (10**9 + 7)