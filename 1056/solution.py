class Solution:
    def confusingNumber(self, N: int) -> bool:
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        num = str(N)
        rotated = []
        for digit in num:
            if int(digit) not in mapping:
                return False
            rotated.append(mapping[int(digit)])
        return int(''.join(rotated[::-1])) != N