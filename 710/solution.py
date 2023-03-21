class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.mapping = {}
        self.non_blacklisted = N - len(blacklist)
        blacklist = set(blacklist)
        last = N - 1
        for num in blacklist:
            if num >= self.non_blacklisted:
                continue
            while last in blacklist:
                last -= 1
            self.mapping[num] = last
            last -= 1

    def pick(self) -> int:
        num = random.randint(0, self.non_blacklisted - 1)
        if num in self.mapping:
            return self.mapping[num]
        return num