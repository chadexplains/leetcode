class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        values = set()
        total_sum = 0
        for node in tree:
            values.add(node.val)
            total_sum += node.val
            for child in node.children:
                total_sum -= child.val
        for val in values:
            total_sum -= val
        for node in tree:
            if node.val == total_sum:
                return node