class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(s):
            return s == s[::-1]
        L = int(left)
        R = int(right)
        MAGIC = 100000
        ans = 0
        # count odd length
        for k in range(MAGIC):
            s = str(k)
            t = s + s[-2::-1] # 11 -> 11, 121 -> 121, 12321 -> 12321
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(str(v)):
                ans += 1
        # count even length
        for k in range(MAGIC):
            s = str(k)
            t = s + s[::-1] # 11 -> 11, 1221 -> 1221, 123321 -> 123321
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(str(v)):
                ans += 1
        return ans