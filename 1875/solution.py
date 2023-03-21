class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        sorted_nums1 = sorted(nums1)
        abs_sum_diff = sum(abs(nums1[i] - nums2[i]) for i in range(len(nums1)))
        max_reduction = 0
        for i in range(len(nums1)):
            j = bisect_left(sorted_nums1, nums2[i])
            if j < len(nums1):
                max_reduction = max(max_reduction, abs(nums1[i] - nums2[i]) - abs(sorted_nums1[j] - nums2[i]))
            if j > 0:
                max_reduction = max(max_reduction, abs(nums1[i] - nums2[i]) - abs(sorted_nums1[j - 1] - nums2[i]))
        return (abs_sum_diff - max_reduction) % MOD