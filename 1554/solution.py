class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = collections.Counter(barcodes)
        barcodes = sorted(barcodes, key=lambda x: (-count[x], x))
        n = len(barcodes)
        res = [0] * n
        res[::2], res[1::2] = barcodes[n // 2:], barcodes[:n // 2]
        if n % 2:
            res[-1] = res[-2]
            res[-2] = barcodes[n // 2 - 1]
        return res