class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        n = len(A)
        ones = sum(A)
        if ones % 3 != 0:
            return [-1, -1]
        if ones == 0:
            return [0, n - 1]
        k = ones // 3
        i = j = l = 0
        for p in range(n):
            if A[p] == 1:
                if i % k == 0:
                    x = p
                if j % k == 0:
                    y = p
                if l % k == 0:
                    z = p
                i += 1
                j += 1
                l += 1
        while z < n and A[x] == A[y] == A[z]:
            x += 1
            y += 1
            z += 1
        if z == n:
            return [x - 1, y]
        return [-1, -1]