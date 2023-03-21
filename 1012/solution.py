def numDupDigitsAtMostN(N):
    digits = list(map(int, str(N + 1)))
    n = len(digits)
    # calculate the number of integers with no repeated digits
    res = 0
    for i in range(1, n):
        res += 9 * A(9, i - 1)
    used = set()
    # calculate the number of integers with at least 1 repeated digit
    for i, x in enumerate(digits):
        for j in range(0 if i else 1, x):
            if j not in used:
                res += A(9 - i, n - i - 1)
        if x in used:
            break
        used.add(x)
    return N - res

# helper function to calculate n choose k
def A(n, k):
    return 1 if k == 0 else A(n - 1, k - 1) * n