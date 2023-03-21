def canReorderDoubled(self, arr: List[int]) -> bool:
    freq = collections.Counter(arr)
    arr.sort()
    for num in arr:
        if freq[num] == 0:
            continue
        if freq[2*num] == 0:
            return False
        freq[num] -= 1
        freq[2*num] -= 1
    return True