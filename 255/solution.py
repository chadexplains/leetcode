class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        min_val = float('-inf')
        for val in preorder:
            if val < min_val:
                return False
            while stack and val > stack[-1]:
                min_val = stack.pop()
            stack.append(val)
        return True