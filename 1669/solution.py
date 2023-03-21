```def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        curr = list1
        while count < a-1:
            curr = curr.next
            count += 1
        start = curr
        while count < b+1:
            curr = curr.next
            count += 1
        end = curr
        curr = list2
        while curr.next:
            curr = curr.next
        start.next = list2
        curr.next = end.next
        return list1```