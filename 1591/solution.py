def swapNodes(self, head: ListNode, k: int) -> ListNode:
    n = 0
    curr = head
    while curr:
        n += 1
        curr = curr.next
    first = head
    second = head
    for i in range(k - 1):
        first = first.next
    for i in range(n - k):
        second = second.next
    first.val, second.val = second.val, first.val
    return head