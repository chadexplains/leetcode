def trailingZeroes(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

def preimageSizeFZF(n: int, left: int, right: int) -> int:
    lo, hi = left, right
    while lo <= hi:
        mid = (lo + hi) // 2
        if trailingZeroes(mid) < n:
            lo = mid + 1
        else:
            hi = mid - 1
    smallest_k = lo
    lo, hi = left, right
    while lo <= hi:
        mid = (lo + hi) // 2
        if trailingZeroes(mid) <= n:
            lo = mid + 1
        else:
            hi = mid - 1
    largest_k = hi
    return largest_k - smallest_k + 1