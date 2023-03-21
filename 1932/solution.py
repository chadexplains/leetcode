```def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    curr = list1
    for i in range(a-1):
        curr = curr.next
    start = curr
    for i in range(b-a+2):
        curr = curr.next
    end = curr
    last = list2
    while last.next:
        last = last.next
    start.next = list2
    last.next = end
    return list1```