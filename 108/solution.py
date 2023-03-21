class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildTree(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = buildTree(left, mid - 1)
            node.right = buildTree(mid + 1, right)
            return node
        return buildTree(0, len(nums) - 1)