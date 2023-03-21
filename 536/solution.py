def str2tree(s):
    if not s:
        return None
    i = 0
    while i < len(s) and (s[i] == '-' or s[i].isdigit()):
        i += 1
    root = TreeNode(int(s[:i]))
    stack = [root]
    j = i
    while j < len(s):
        if s[j] == '(':  # start of left subtree
            i = j + 1
            count = 1
            while count != 0:
                if s[i] == '(':  # nested left subtree
                    count += 1
                elif s[i] == ')':  # end of left subtree
                    count -= 1
                i += 1
            node = str2tree(s[j+1:i-1])
            if stack[-1].left:
                stack[-1].right = node
            else:
                stack[-1].left = node
            stack.append(node)
            j = i
        elif s[j] == ')':  # end of current subtree
            stack.pop()
            j += 1
        else:  # start of right subtree
            i = j + 1
            while i < len(s) and (s[i] == '-' or s[i].isdigit()):
                i += 1
            node = TreeNode(int(s[j+1:i]))
            if stack[-1].left:
                stack[-1].right = node
            else:
                stack[-1].left = node
            stack.append(node)
            j = i
    return root