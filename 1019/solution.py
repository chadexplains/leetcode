def nextLargerNodes(head):
    stack = []
    result = []
    while head:
        while stack and stack[-1][1] < head.val:
            i, _ = stack.pop()
            result[i] = head.val
        stack.append((len(result), head.val))
        result.append(0)
        head = head.next
    return result