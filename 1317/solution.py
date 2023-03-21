class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        A, B = 1, n-1
        while '0' in str(A) or '0' in str(B):
            A += 1
            B -= 1
        return [A, B]