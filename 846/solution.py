class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        if len(hand) % k != 0:
            return False
        freq = collections.Counter(hand)
        cards = sorted(freq.keys())
        groups = []
        for card in cards:
            count = freq[card]
            if count == 0:
                continue
            if len(groups) == 0 or card != groups[-1][-1] + 1:
                if count < k:
                    return False
                group = [card]
                for i in range(1, k):
                    group.append(card + i)
                groups.append(group)
                for c in group:
                    freq[c] -= 1
            else:
                group = groups.pop()
                for i in range(k):
                    if freq[card + i] < group.count(group[0]):
                        return False
                    freq[card + i] -= group.count(group[0])
                    if freq[card + i] == 0:
                        del freq[card + i]
                group.append(card + k - 1)
                groups.append(group)
        return True