class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ''
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            temp_sum = n1 + n2 + carry
            carry = temp_sum // 10
            res = str(temp_sum % 10) + res
            i -= 1
            j -= 1
        if carry:
            res = '1' + res
        return res