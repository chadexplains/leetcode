class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        insertions = 0
        for c in s:
            if c == '(': # opening bracket
                stack.append(c)
            else: # closing bracket
                if not stack or stack[-1] == ')': # need to insert opening bracket
                    insertions += 1
                    stack.append('(')
                if stack and stack[-1] == '(': # found matching pair
                    stack.pop()
                if not stack or stack[-1] == ')': # need to insert closing bracket
                    insertions += 1
                    if stack: # pop the opening bracket
                        stack.pop()
        insertions += len(stack) * 2 # insert closing brackets for remaining opening brackets
        return insertions