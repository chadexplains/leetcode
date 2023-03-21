def checkEquivalence(root1: 'Node', root2: 'Node') -> bool:
    stack = [(root1, root2)]
    while stack:
        node1, node2 = stack.pop()
        if not node1 and not node2:
            continue
        if not node1 or not node2 or node1.val != node2.val:
            return False
        if node1.left and node2.left:
            stack.append((node1.left, node2.left))
        elif node1.left or node2.left:
            return False
        if node1.right and node2.right:
            stack.append((node1.right, node2.right))
        elif node1.right or node2.right:
            return False
    return True