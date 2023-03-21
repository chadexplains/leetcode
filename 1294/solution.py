def isPossibleDivide(nums: List[int], k: int) -> bool:
    freq = collections.Counter(nums)
    nums.sort()
    for num in nums:
        if freq[num] > 0:
            for i in range(num, num + k):
                if freq[i] == 0:
                    return False
                freq[i] -= 1
    return True