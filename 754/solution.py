class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = math.ceil((-1 + math.sqrt(1 + 8 * target)) / 2)
        total = n * (n + 1) // 2
        diff = total - target
        if diff % 2 == 0:
            return n
        else:
            return n + 1 + (n % 2)