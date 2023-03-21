class Solution:
    def modifyString(self, s: str) -> str:
        prev = ''
        s = list(s)
        for i in range(len(s)):
            if s[i] != '?':
                prev = s[i]
            else:
                for c in 'abcde':
                    if c != prev:
                        s[i] = c
                        prev = c
                        break
        return ''.join(s)