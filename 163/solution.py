class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if curr - prev > 1:
                result.append(self.getRange(prev + 1, curr - 1))
            prev = curr
        return result
    
    def getRange(self, start: int, end: int) -> str:
        if start == end:
            return str(start)
        else:
            return str(start) + "->" + str(end)