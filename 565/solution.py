class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_length = 0
        visited = set()
        for i in range(len(nums)):
            if i not in visited:
                length = 0
                j = i
                while j not in visited:
                    visited.add(j)
                    j = nums[j]
                    length += 1
                max_length = max(max_length, length)
        return max_length