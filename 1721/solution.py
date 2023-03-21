def swapNodes(self, head: ListNode, k: int) -> ListNode:
    first = second = head
    for i in range(k - 1):
        first = first.next
    end = first
    while end.next:
        second = second.next
        end = end.next
    first.val, second.val = second.val, first.val
    return head