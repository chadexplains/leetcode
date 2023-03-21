def findKthBit(n: int, k: int) -> str:
    if n == 1:
        return "0"
    length = 2**n - 1
    mid = length // 2
    if k == mid + 1:
        return "1"
    elif k < mid + 1:
        return findKthBit(n-1, k)
    else:
        return str(1 - int(findKthBit(n-1, k-(mid+1))))