class Solution:
    def readBinaryWatch(self, n: int) -> List[str]:
        times = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == n:
                    times.append(f'{h}:{m:02d}')
        return times