class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        for i in range(32):
            set_bits = 0
            for num in nums:
                set_bits += (num >> i) & 1
            unset_bits = len(nums) - set_bits
            total_distance += set_bits * unset_bits
        return total_distance