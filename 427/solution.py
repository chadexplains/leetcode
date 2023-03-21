class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(x1, y1, x2, y2):
            if x1 == x2 and y1 == y2:
                return Node(grid[x1][y1] == 1, True, None, None, None, None)
            node = Node(False, False, None, None, None, None)
            xm, ym = (x1 + x2) // 2, (y1 + y2) // 2
            node.topLeft = build(x1, y1, xm, ym)
            node.topRight = build(x1, ym + 1, xm, y2)
            node.bottomLeft = build(xm + 1, y1, x2, ym)
            node.bottomRight = build(xm + 1, ym + 1, x2, y2)
            if node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val == node.val:
                node.isLeaf = True
                node.topLeft = node.topRight = node.bottomLeft = node.bottomRight = None
            return node
        return build(0, 0, len(grid) - 1, len(grid) - 1)