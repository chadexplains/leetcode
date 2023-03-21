class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = collections.defaultdict(int)
        for row, seat in reservedSeats:
            reserved[row] |= 1 << (seat - 1)
        count = (n - len(reserved)) * 2
        for row in reserved:
            if not (reserved[row] & 30):
                count += 1
            if not (reserved[row] & 480):
                count += 1
            elif not (reserved[row] & 60):
                count += 1
        return count