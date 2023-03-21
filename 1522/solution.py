class Solution:
    def diameter(self, root: 'Node') -> int:
        self.max1 = 0
        self.max2 = 0
        
        def helper(node):
            if not node:
                return 0
            max_child = 0
            for child in node.children:
                child_len = helper(child)
                if child_len > max_child:
                    max_child, second_max_child = child_len, max_child
                elif child_len > second_max_child:
                    second_max_child = child_len
            self.max1 = max(self.max1, max_child + second_max_child)
            return max_child + 1
        
        helper(root)
        return self.max1