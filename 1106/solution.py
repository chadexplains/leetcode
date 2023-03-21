class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c == ')':
                operands = []
                while stack[-1] != '(': # Evaluate the expression
                    operands.append(stack.pop())
                stack.pop() # Pop the opening parenthesis
                operator = stack.pop()
                if operator == '&':
                    result = all(operands)
                elif operator == '|':
                    result = any(operands)
                else: # operator == '!'
                    result = not operands[0]
                stack.append(result)
            elif c.isalpha():
                stack.append(c == 't') # Convert 't' to True and 'f' to False
            elif c in '&|!(': # Push operators onto the stack
                stack.append(c)
        return stack[0]