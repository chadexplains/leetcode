def numDupDigitsAtMostN(N: int) -> int:
    digits = [int(x) for x in str(N + 1)]
    n = len(digits)
    no_repeat = 0
    for i in range(1, n):
        no_repeat += 9 * A(9, i - 1)
    seen = set()
    for i, x in enumerate(digits):
        for y in range(0 if i else 1, x):
            if y not in seen:
                no_repeat += A(9 - i, n - i - 1)
        if x in seen:
            break
        seen.add(x)
    else:
        no_repeat += 1
    return N - no_repeat

def A(m, n):
    return 1 if n == 0 else A(m, n - 1) * (m - n + 1)