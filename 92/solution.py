def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    for i in range(m-1):
        prev = prev.next
    curr = prev.next
    for i in range(n-m):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
    return dummy.next