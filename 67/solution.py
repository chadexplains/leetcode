class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            s = x + y + carry
            carry = s // 2
            res.append(str(s % 2))
            i -= 1
            j -= 1
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1])