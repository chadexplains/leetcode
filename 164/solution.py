class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        n = len(nums)
        min_gap = math.ceil((max_val - min_val) / (n - 1))
        buckets_min = [float('inf')] * (n - 1)
        buckets_max = [float('-inf')] * (n - 1)
        for num in nums:
            if num == min_val or num == max_val:
                continue
            idx = (num - min_val) // min_gap
            buckets_min[idx] = min(buckets_min[idx], num)
            buckets_max[idx] = max(buckets_max[idx], num)
        max_gap = float('-inf')
        prev_max = min_val
        for i in range(n - 1):
            if buckets_min[i] == float('inf'):
                continue
            max_gap = max(max_gap, buckets_min[i] - prev_max)
            prev_max = buckets_max[i]
        max_gap = max(max_gap, max_val - prev_max)
        return max_gap