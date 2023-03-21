def isCousins(root, x, y):
    queue = [(root, 0, None)]
    found_x = False
    found_y = False
    while queue:
        node, depth, parent = queue.pop(0)
        if node.val == x:
            found_x = (depth, parent)
        elif node.val == y:
            found_y = (depth, parent)
        if found_x and found_y:
            return found_x[0] == found_y[0] and found_x[1] != found_y[1]
        if node.left:
            queue.append((node.left, depth+1, node))
        if node.right:
            queue.append((node.right, depth+1, node))
    return False