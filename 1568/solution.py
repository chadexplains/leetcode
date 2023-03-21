class Solution:
    def findLatestStep(self, nums: List[int], m: int) -> int:
        n = len(nums)
        groups = [1] * n
        lengths = {1: n}
        count = 0
        for i, num in enumerate(nums):
            if num == 1:
                if i > 0 and nums[i-1] == 0:
                    left = groups[i-1]
                    right = groups[i]
                    lengths[left+right] = lengths.get(left+right, 0) + 1
                    lengths[left] -= 1
                    lengths[right] -= 1
                    if lengths[left] == 0:
                        del lengths[left]
                    if lengths[right] == 0:
                        del lengths[right]
                    groups[i-left:i+1] = [left+right] * (left+right)
            if m in lengths.values():
                count = i + 1
        return count