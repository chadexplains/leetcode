def findPermutation(n: int, s: str) -> List[int]:
    nums = list(range(1, n+1))
    i = 0
    while i < len(s):
        if s[i] == 'D':
            j = i
            while j < len(s) and s[j] == 'D':
                j += 1
            nums[i:j+1] = reversed(nums[i:j+1])
            i = j
        else:
            i += 1
    return nums