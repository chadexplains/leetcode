class Solution:
    
def __init__(self, head: ListNode):
        self.head = head
        
def getRandom(self) -> int:
        result = self.head.val
        node = self.head.next
        count = 1
        while node:
            if random.randint(0, count) == 0:
                result = node.val
            node = node.next
            count += 1
        return result