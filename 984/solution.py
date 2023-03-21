class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        res = ''
        while A or B:
            if len(res) >= 2 and res[-2:] == 'aa':
                res += 'b'
                B -= 1
            elif len(res) >= 2 and res[-2:] == 'bb':
                res += 'a'
                A -= 1
            elif A >= B:
                res += 'a'
                A -= 1
            else:
                res += 'b'
                B -= 1
        return res