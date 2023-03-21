class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        deque = collections.deque([0])
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if deque[0] < i - k:
                deque.popleft()
            dp[i] = max(nums[i], nums[i] + dp[deque[0]])
            while deque and dp[i] >= dp[deque[-1]]:
                deque.pop()
            deque.append(i)
        return max(dp)