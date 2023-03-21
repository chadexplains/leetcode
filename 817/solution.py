class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        gset = set(G)
        cur = head
        ans = 0
        while cur:
            if cur.val in gset and (not cur.next or cur.next.val not in gset):
                ans += 1
            cur = cur.next
        return ans