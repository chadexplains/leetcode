class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        if p == q:
            return root
        if p == root:
            new_root = p.children.pop()
            q.children.append(p)
            p.children.append(new_root)
            return q
        parent_p = self.find_parent(root, p)
        parent_p.children.remove(p)
        q.children.append(p)
        return root

    def find_parent(self, root, node):
        if node in root.children:
            return root
        for child in root.children:
            parent = self.find_parent(child, node)
            if parent:
                return parent
        return None