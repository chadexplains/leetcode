class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        stack = []
        for node in nodes:
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack[-1] = '#'
        return len(stack) == 1 and stack[0] == '#'