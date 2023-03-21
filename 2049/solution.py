class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        counts = {0: 1}
        for num in nums:
            for bitwise_or, count in list(counts.items()):
                new_bitwise_or = bitwise_or | num
                if new_bitwise_or not in counts:
                    counts[new_bitwise_or] = 0
                counts[new_bitwise_or] += count
        return counts[max_or]