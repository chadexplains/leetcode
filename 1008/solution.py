class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        split_index = len(preorder)
        for i in range(1, len(preorder)):
            if preorder[i] > root.val:
                split_index = i
                break
        root.left = self.bstFromPreorder(preorder[1:split_index])
        root.right = self.bstFromPreorder(preorder[split_index:])
        return root