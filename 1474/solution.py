def deleteNodes(head: ListNode, m: int, n: int) -> ListNode:
    curr = head
    prev = None
    count = 0
    while curr:
        count += 1
        if count == m:
            flag = True
            prev = curr
            curr = curr.next
            count = 0
        elif flag and count < n:
            curr = curr.next
            count += 1
        elif flag and count == n:
            flag = False
            prev.next = curr.next
            curr = prev.next
            count = 0
        else:
            prev = curr
            curr = curr.next
    return head