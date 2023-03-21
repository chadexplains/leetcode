def canReorderDoubled(self, arr: List[int]) -> bool:
    arr.sort()
    freq = collections.Counter(arr)
    for num in arr:
        if freq[num] == 0:
            continue
        if freq[num * 2] == 0:
            return False
        freq[num] -= 1
        freq[num * 2] -= 1
    return True