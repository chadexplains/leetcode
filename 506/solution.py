class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        sorted_nums = sorted(nums, reverse=True)
        ranks = {sorted_nums[i]: str(i+1) for i in range(len(sorted_nums))}
        medals = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        result = []
        for num in nums:
            if ranks[num] in medals:
                result.append(medals[ranks[num]])
            else:
                result.append(ranks[num])
        return result