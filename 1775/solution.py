def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
    diff = sum(nums2) - sum(nums1)
    if diff < 0:
        nums1, nums2 = nums2, nums1
        diff = -diff
    if diff == 0:
        return 0
    nums1.sort(reverse=True)
    nums2.sort()
    i, j, count = 0, 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] - 1 >= 6 - nums2[j]:
            nums1[i] -= (6 - nums2[j])
            j += 1
        else:
            nums1[i] -= 1
        count += 1
        if sum(nums1) < sum(nums2):
            return count
        if nums1[i] == 0:
            i += 1
    return -1