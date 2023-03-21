def median(nums, freq):
    arr = []
    for i in range(len(nums)):
        arr.extend([nums[i]] * freq[i])
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        return arr[n // 2]