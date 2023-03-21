class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = second_largest = -1
        index = -1
        for i, num in enumerate(nums):
            if num >= largest:
                second_largest = largest
                largest = num
                index = i
            elif num >= second_largest:
                second_largest = num
        return index if largest >= 2 * second_largest else -1