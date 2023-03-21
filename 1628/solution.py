class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, tokens: List[str]) -> 'Node':
        stack = []
        for token in tokens:
            if token.isdigit():
                stack.append(Node(int(token)))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(token, left, right))
        return stack.pop()

    def evaluate(self, root: 'Node') -> int:
        if root.val.isdigit():
            return int(root.val)
        left_val = self.evaluate(root.left)
        right_val = self.evaluate(root.right)
        if root.val == '+':
            return left_val + right_val
        elif root.val == '-':
            return left_val - right_val
        elif root.val == '*':
            return left_val * right_val
        else:
            return left_val // right_val