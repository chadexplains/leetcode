class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heap.append((l.val, i, l))
        heapq.heapify(heap)
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
        return dummy.next