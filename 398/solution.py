class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        index = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                if random.randint(1, count) == 1:
                    index = i
        return index