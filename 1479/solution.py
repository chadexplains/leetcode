def kthFactor(n: int, k: int) -> int:
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    if int(n**0.5)**2 == n:
        factors.remove(int(n**0.5))
    return -1 if len(factors) < k else factors[k-1]