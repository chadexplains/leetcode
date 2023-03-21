def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
    even_sum = sum(x for x in A if x % 2 == 0)
    res = []
    for val, index in queries:
        if A[index] % 2 == 0:
            even_sum -= A[index]
        A[index] += val
        if A[index] % 2 == 0:
            even_sum += A[index]
        res.append(even_sum)
    return res