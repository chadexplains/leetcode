class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        sums1 = self.generateSums(nums[:n//2])
        sums2 = self.generateSums(nums[n//2:])
        sums2.sort()
        ans = float('inf')
        for s in sums1:
            i = bisect_left(sums2, goal - s)
            if i < len(sums2):
                ans = min(ans, abs(goal - s - sums2[i]))
            if i > 0:
                ans = min(ans, abs(goal - s - sums2[i-1]))
        return ans
    def generateSums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sums = [0]
        for i in range(n):
            for j in range(len(sums)):
                sums.append(sums[j] + nums[i])
        return sums