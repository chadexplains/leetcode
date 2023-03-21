def minMoves(self, nums: List[int], limit: int) -> int:
    freq = defaultdict(int)
    n = len(nums)
    for i in range(n // 2):
        s = nums[i] + nums[n - 1 - i]
        freq[s] += 1
    ans = n
    for s in range(2, 2 * limit + 1):
        if s not in freq:
            continue
        moves = n // 2 - freq[s]
        if s > limit + 1:
            moves += freq[s - limit - 1]
        if s < 2 * limit:
            moves += freq[s - 1]
        ans = min(ans, moves)
    return ans