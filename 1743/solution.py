def restoreArray(adjacentPairs):
    nums = []
    pairs = {}
    for pair in adjacentPairs:
        pairs[pair[0]] = pairs.get(pair[0], []) + [pair[1]]
        pairs[pair[1]] = pairs.get(pair[1], []) + [pair[0]]
    for key in pairs:
        if len(pairs[key]) == 1:
            nums.append(key)
            break
    prev = nums[0]
    curr = pairs[prev][0]
    nums.append(curr)
    while len(nums) < len(pairs) + 1:
        temp = curr
        curr = pairs[curr][0] if pairs[curr][0] != prev else pairs[curr][1]
        prev = temp
        nums.append(curr)
    return nums