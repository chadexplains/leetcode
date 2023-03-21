class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, num):
        node = self.root
        for bit in f'{num:032b}':
            node = node.setdefault(bit, {})

    def find_max_xor(self, num):
        node = self.root
        xor = 0
        for bit in f'{num:032b}':
            toggled_bit = '1' if bit == '0' else '0'
            if toggled_bit in node:
                xor |= (1 << 31)
                node = node[toggled_bit]
            else:
                node = node[bit]
        return xor

def findMaximumXOR(nums):
    trie = Trie()
    for num in nums:
        trie.insert(num)
    max_xor = 0
    for num in nums:
        max_xor = max(max_xor, trie.find_max_xor(num) ^ num)
    return max_xor