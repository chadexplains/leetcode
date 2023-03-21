def splitListToParts(root: ListNode, k: int) -> List[ListNode]:
    n, curr = 0, root
    while curr:
        n += 1
        curr = curr.next
    width, remainder = divmod(n, k)
    res = []
    curr = root
    for i in range(k):
        head = curr
        for j in range(width + (i < remainder) - 1):
            if curr:
                curr = curr.next
        if curr:
            curr.next, curr = None, curr.next
        res.append(head)
    return res