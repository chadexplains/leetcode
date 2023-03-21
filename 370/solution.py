def getModifiedArray(length, updates):
    arr = [0] * (length + 1)
    for start, end, inc in updates:
        arr[start] += inc
        arr[end+1] -= inc
    for i in range(1, length):
        arr[i] += arr[i-1]
    return arr[:-1]