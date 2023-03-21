class CBTInserter:
    
    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = [root]
        while self.queue:
            node = self.queue[0]
            if not node.left or not node.right:
                break
            self.queue.append(node.left)
            self.queue.append(node.right)
            self.queue.pop(0)
        
    def insert(self, v: int) -> int:
        node = TreeNode(v)
        parent = self.queue[0]
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            self.queue.pop(0)
            if parent.right:
                self.queue.append(parent.left)
                self.queue.append(parent.right)
        return parent.val
    
    def get_root(self) -> TreeNode:
        return self.root