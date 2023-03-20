class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        p2 = p3 = p5 = 0
        for i in range(1, n):
            u = min(ugly[p2]*2, ugly[p3]*3, ugly[p5]*5)
            ugly.append(u)
            if u == ugly[p2]*2:
                p2 += 1
            if u == ugly[p3]*3:
                p3 += 1
            if u == ugly[p5]*5:
                p5 += 1
        return ugly[-1]