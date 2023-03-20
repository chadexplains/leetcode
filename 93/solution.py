class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, segments):
            if len(segments) == 4 and start == len(s):
                res.append('.'.join(segments))
                return
            if len(segments) == 4 or start == len(s):
                return
            for i in range(start, min(start + 3, len(s))):
                if i > start and s[start] == '0':
                    return
                segment = s[start:i+1]
                if int(segment) > 255:
                    return
                segments.append(segment)
                backtrack(i+1, segments)
                segments.pop()
        res = []
        backtrack(0, [])
        return res