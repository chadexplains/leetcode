class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq = collections.Counter(nums)
        count = 0
        used = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and (i, j) not in used and (j, i) not in used and nums[i] + nums[j] == target:
                    count += 1
                    used.add((i, j))
                    used.add((j, i))
        return count