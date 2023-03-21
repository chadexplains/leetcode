class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_indices = [-1] + [i for i in range(len(nums)) if nums[i] % 2 == 1] + [len(nums)]
        count = 0
        for i in range(k, len(odd_indices) - k):
            count += (odd_indices[i] - odd_indices[i-k]) * (odd_indices[i+k] - odd_indices[i+k-1])
        return count