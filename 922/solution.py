def sortArrayByParityII(A):
    even, odd = 0, 1
    while even < len(A) and odd < len(A):
        if A[even] % 2 == 1 and A[odd] % 2 == 0:
            A[even], A[odd] = A[odd], A[even]
        if A[even] % 2 == 0:
            even += 2
        if A[odd] % 2 == 1:
            odd += 2
    return A