class Solution:
    def calculate(self, s: str) -> int:
        # Convert infix to postfix
        postfix = self.infix_to_postfix(s)
        # Evaluate postfix
        stack = []
        for token in postfix:
            if token.isdigit():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
                elif token == '^':
                    stack.append(a ** b)
        return stack.pop()

    def infix_to_postfix(self, s: str) -> List[str]:
        # Shunting yard algorithm
        output = []
        stack = []
        prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        associativity = {'+': 'left', '-': 'left', '*': 'left', '/': 'left', '^': 'right'}
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                output.append(s[i:j])
                i = j
            elif s[i] in prec:
                while stack and stack[-1] != '(':
                    if (associativity[s[i]] == 'left' and prec[s[i]] <= prec[stack[-1]]) or (associativity[s[i]] == 'right' and prec[s[i]] < prec[stack[-1]]):
                        output.append(stack.pop())
                    else:
                        break
                stack.append(s[i])
                i += 1
            elif s[i] == '(':  
                stack.append(s[i])
                i += 1
            elif s[i] == ')':
                while stack and stack[-1] != '(':  
                    output.append(stack.pop())
                stack.pop()
                i += 1
            else:
                i += 1
        while stack:
            output.append(stack.pop())
        return output