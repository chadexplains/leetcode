class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        for group in groups:
            found = False
            while i <= len(nums) - len(group):
                if nums[i:i+len(group)] == group:
                    found = True
                    i += len(group)
                    break
                i += 1
            if not found:
                return False
        return True