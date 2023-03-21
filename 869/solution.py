class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        digits = sorted(str(N))
        for i in range(31):
            if digits == sorted(str(1 << i)):
                return True
        return False