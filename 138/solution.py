class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        node_map = {}
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            node_map[curr].next = node_map.get(curr.next)
            node_map[curr].random = node_map.get(curr.random)
            curr = curr.next
        return node_map[head]