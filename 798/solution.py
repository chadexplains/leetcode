class Solution:
    def bestRotation(self, A: List[int]) -> int:
        n = len(A)
        bad = [0] * n
        for i in range(n):
            left, right = (i - A[i] + 1) % n, (i + 1) % n
            bad[left] -= 1
            bad[right] += 1
            if left > right:
                bad[0] -= 1
        best = -n
        ans = cur = 0
        for i in range(n):
            cur += bad[i]
            if cur > best:
                best = cur
                ans = i
        return ans