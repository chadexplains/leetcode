class Solution:
    def countDigitOne(self, n: int) -> int:
        n_str = str(n)
        count = 0
        for i, digit in enumerate(n_str):
            left = int(n_str[:i]) if i > 0 else 0
            right = int(n_str[i+1:]) if i < len(n_str)-1 else 0
            if digit == '0':
                count += left * (10 ** (len(n_str)-i-1))
            elif digit == '1':
                count += left * (10 ** (len(n_str)-i-1)) + right + 1
            else:
                count += (left + 1) * (10 ** (len(n_str)-i-1))
        return count