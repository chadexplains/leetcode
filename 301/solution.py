class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0
            for c in s:
                if c == '(': count += 1
                elif c == ')': count -= 1
                if count < 0: return False
            return count == 0
        level = {s}
        while True:
            valid = list(filter(is_valid, level))
            if valid: return valid
            next_level = set()
            for s in level:
                for i in range(len(s)):
                    if s[i] in '()':
                        next_level.add(s[:i] + s[i+1:])
            level = next_level
