class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        freq = collections.Counter(nums2)
        count = 0
        for x in nums1:
            for y, z in itertools.combinations_with_replacement(nums2, 2):
                if y * z == x * x:
                    if y == z:
                        count += freq[y] * (freq[y] - 1) // 2
                    else:
                        count += freq[y] * freq[z]
        return count