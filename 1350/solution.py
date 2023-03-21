def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    freq_list = sorted(freq.values(), reverse=True)
    requests.sort(key=lambda x: x[1], reverse=True)
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix_sum[i+1] = prefix_sum[i] + nums[i]
    ans = 0
    for i in range(len(requests)):
        xi, mi = requests[i]
        if freq_list[i] == 0:
            break
        ans += xi * freq_list[i] * (prefix_sum[mi+1] - prefix_sum[mi])
    return ans % (10**9 + 7)