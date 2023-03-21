class Solution:
    def findNthDigit(self, n: int) -> int:
        len_num = 1
        count = 9
        start = 1
        while n > len_num * count:
            n -= len_num * count
            len_num += 1
            count *= 10
            start *= 10
        start += (n - 1) // len_num
        return int(str(start)[(n - 1) % len_num])