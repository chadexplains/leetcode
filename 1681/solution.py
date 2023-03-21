class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums) - min(nums)
        if k == 1:
            return sum(max(nums[i:i+n//k]) - min(nums[i:i+n//k]) for i in range(0, n, n//k))
        if k > n//2:
            return -1
        nums.sort()
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1, 1 << n):
            if bin(mask).count('1') % (n // k) == 0:
                subarrays = []
                for i in range(n):
                    if mask & (1 << i):
                        subarrays.append(nums[i])
                if len(set(subarrays)) == len(subarrays):
                    dp[mask] = max(subarrays) - min(subarrays)
                else:
                    for submask in range(mask):
                        if submask & mask == submask:
                            dp[mask] = min(dp[mask], dp[submask] + dp[mask ^ submask])
        return dp[(1 << n) - 1]