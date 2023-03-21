class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node: TreeNode, arr: List[int]) -> None:
            if not node:
                return
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)
        arr1, arr2 = [], []
        inorder(root1, arr1)
        inorder(root2, arr2)
        return sorted(arr1 + arr2)