class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []
        num = 0
        for i in range(len(A)):
            num = (num * 2 + A[i]) % 5
            result.append(num == 0)
        return result