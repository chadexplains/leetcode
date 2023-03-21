class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainders = collections.defaultdict(int)
        for num in arr:
            remainders[num % k] += 1
        for remainder in remainders:
            if remainder == 0:
                if remainders[remainder] % 2 != 0:
                    return False
            elif remainders[remainder] != remainders[k - remainder]:
                return False
        return True