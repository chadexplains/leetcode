class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def generate(s):
            n = len(s)
            if n == 1:
                return [s]
            if s[0] == '0' and s[-1] == '0':
                return []
            if s[0] == '0':
                return [s[0] + '.' + s[1:]]
            if s[-1] == '0':
                return [s]
            res = [s]
            for i in range(1, n):
                res.append(s[:i] + '.' + s[i:])
            return res
        s = s[1:-1]
        n = len(s)
        res = []
        for i in range(1, n):
            left = generate(s[:i])
            right = generate(s[i:])
            for l in left:
                for r in right:
                    res.append('(' + l + ', ' + r + ')')
        return res