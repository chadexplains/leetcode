def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
    A.sort()
    B_with_idx = sorted([(b, i) for i, b in enumerate(B)])
    ans = [-1] * len(A)
    j = 0
    for a in A:
        if a > B_with_idx[j][0]:
            ans[B_with_idx[j][1]] = a
            j += 1
        else:
            ans[B_with_idx[-1][1]] = a
            B_with_idx.pop()
    return ans