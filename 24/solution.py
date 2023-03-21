def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        current.next = second
        first.next = second.next
        second.next = first
        current = current.next.next
    return dummy.next