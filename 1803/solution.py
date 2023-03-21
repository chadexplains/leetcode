class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def count_pairs(self, num, low, high):
        node = self.root
        count = 0
        for i in range(31, -1, -1):
            if not node:
                break
            bit_num = (num >> i) & 1
            bit_low = (low >> i) & 1
            bit_high = (high >> i) & 1
            if bit_low == 1 and bit_high == 1:
                if 0 in node and 1 in node:
                    count += (1 << i)
                node = node[bit_num]
            elif bit_low == 1:
                if 0 in node:
                    count += (1 << i)
                node = node[1]
            elif bit_high == 1:
                if 1 in node:
                    count += (1 << i)
                node = node[0]
            else:
                node = node[bit_num]
        return count


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie()
        count = 0
        for num in nums:
            count += trie.count_pairs(num, low, high)
            trie.insert(num)
        return count