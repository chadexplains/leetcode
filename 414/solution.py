class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top3 = set()
        for num in nums:
            top3.add(num)
            if len(top3) > 3:
                top3.remove(min(top3))
        return max(top3) if len(top3) < 3 else min(top3)