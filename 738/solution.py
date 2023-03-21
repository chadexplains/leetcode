def monotoneIncreasingDigits(N):
    digits = [int(d) for d in str(N)]
    n = len(digits)
    for i in range(n-1, 0, -1):
        if digits[i] < digits[i-1]:
            digits[i-1] -= 1
            digits[i:] = [9] * (n-i)
    return int(''.join(map(str, digits)))