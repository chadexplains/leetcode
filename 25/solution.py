def reverseKGroup(head, k):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while prev:
        prev = reverse(prev, k)
    return dummy.next


def reverse(prev, k):
    last = prev
    for i in range(k + 1):
        last = last.next
        if i != k and not last:
            return None
    tail = prev.next
    curr = prev.next.next
    while curr != last:
        next_node = curr.next
        curr.next = prev.next
        prev.next = curr
        tail.next = next_node
        curr = next_node
    return tail