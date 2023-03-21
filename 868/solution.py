class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        last_one = None
        max_distance = 0
        for i, bit in enumerate(binary):
            if bit == '1':
                if last_one is not None:
                    distance = i - last_one
                    max_distance = max(max_distance, distance)
                last_one = i
        return max_distance