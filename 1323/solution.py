class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        i = s.find('6')
        if i != -1:
            s = s[:i] + '9' + s[i+1:]
        return int(s)