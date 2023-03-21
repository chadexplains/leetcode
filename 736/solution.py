class Solution:
    def evaluate(self, expression: str) -> int:
        def parse(tokens):
            if tokens[0] == 'add':
                return parse(tokens[1:]) + parse(tokens[1 + parse(tokens[1:]) + 1:])
            elif tokens[0] == 'mult':
                return parse(tokens[1:]) * parse(tokens[1 + parse(tokens[1:]) + 1:])
            else:
                for i in range(1, len(tokens), 2):
                    if tokens[i] == tokens[1]:
                        return parse(tokens[i + 1:])
                return variables[tokens[1]] if tokens[1] in variables else int(tokens[1])
        variables = {}
        tokens, i = [], 0
        while i < len(expression):
            if expression[i] != ' ':
                if expression[i] == '(':
                    tokens.append(expression[i])
                elif expression[i] == ')':
                    tokens.append(expression[i])
                else:
                    j = i
                    while j < len(expression) and expression[j] not in (' ', ')'):
                        if j == i and expression[j] == '-':
                            j += 1
                        j += 1
                    tokens.append(expression[i:j])
                    i = j - 1
            i += 1
        return parse(tokens)