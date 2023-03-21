```def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    curr = list1
    for i in range(a-1):
        curr = curr.next
    start = curr
    for i in range(b-a+1):
        curr = curr.next
    end = curr.next
    curr = list2
    while curr.next:
        curr = curr.next
    start.next = list2
    curr.next = end
    return list1```