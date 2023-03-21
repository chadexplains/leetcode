class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        arr = [0] * n
        for i in range(k+1):
            arr[i] = i//2 + 1 if i % 2 == 0 else k+1 - i//2
        for i in range(k+1, n):
            arr[i] = i+1
        return arr