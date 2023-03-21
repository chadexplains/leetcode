class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1
        s = [0] * (n + 1)
        s[0], s[1], s[2] = 1, 2, 2
        head, tail, num, res = 2, 3, 1, 1
        while tail < n:
            for i in range(s[head]):
                s[tail] = num
                if num == 1 and tail < n:
                    res += 1
                tail += 1
                if tail == n:
                    break
            num = 3 - num
            head += 1
        return res