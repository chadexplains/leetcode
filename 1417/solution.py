class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []
        for c in s:
            if c.isalpha():
                letters.append(c)
            else:
                digits.append(c)
        if abs(len(letters) - len(digits)) > 1:
            return ""
        result = []
        if len(letters) > len(digits):
            for i in range(len(digits)):
                result.append(letters[i])
                result.append(digits[i])
            result.append(letters[-1])
        elif len(digits) > len(letters):
            for i in range(len(letters)):
                result.append(digits[i])
                result.append(letters[i])
            result.append(digits[-1])
        else:
            for i in range(len(letters)):
                result.append(letters[i])
                result.append(digits[i])
        return ''.join(result)