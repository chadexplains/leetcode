class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def subtree_sum(node):
            if not node:
                return 0
            return node.val + subtree_sum(node.left) + subtree_sum(node.right)
        total_sum = subtree_sum(root)
        max_product = 0
        def find_max_product(node):
            nonlocal max_product
            if not node:
                return 0
            left_sum = find_max_product(node.left)
            right_sum = find_max_product(node.right)
            subtree = left_sum + right_sum + node.val
            product = subtree * (total_sum - subtree)
            max_product = max(max_product, product)
            return subtree
        find_max_product(root)
        return max_product % (10**9 + 7)