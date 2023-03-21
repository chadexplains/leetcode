def findBestValue(arr, target):
    arr.sort()
    n = len(arr)
    prefix = [0] * n
    for i in range(n):
        prefix[i] = prefix[i - 1] + arr[i]
    l, r, ans = 0, arr[-1], -1
    while l <= r:
        mid = (l + r) // 2
        idx = bisect_left(arr, mid)
        cur = prefix[idx - 1] + (n - idx) * mid
        if cur <= target:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    def check(x):
        return sum(x if num > x else num for num in arr)
    if ans == -1:
        return min(arr, key=lambda x: abs(x - target))
    return ans if abs(check(ans) - target) <= abs(check(ans + 1) - target) else ans + 1