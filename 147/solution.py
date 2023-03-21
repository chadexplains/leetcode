class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = head
        while curr:
            prev = dummy
            next_node = prev.next
            while next_node:
                if curr.val < next_node.val:
                    break
                prev = next_node
                next_node = prev.next
            temp = curr.next
            curr.next = next_node
            prev.next = curr
            curr = temp
        return dummy.next