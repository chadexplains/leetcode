class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        def height_and_diameter(node):
            if node is None:
                return 0, 0
            left_height, left_diameter = height_and_diameter(node.left)
            right_height, right_diameter = height_and_diameter(node.right)
            current_diameter = max(left_diameter, right_diameter, left_height + right_height)
            current_height = max(left_height, right_height) + 1
            self.diameter = max(self.diameter, current_diameter)
            return current_height, current_diameter
        height_and_diameter(root)
        return self.diameter