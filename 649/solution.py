class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_q = deque()
        dire_q = deque()
        n = len(senate)
        for i, s in enumerate(senate):
            if s == 'R':
                radiant_q.append(i)
            else:
                dire_q.append(i)
        while radiant_q and dire_q:
            radiant_idx = radiant_q.popleft()
            dire_idx = dire_q.popleft()
            if radiant_idx < dire_idx:
                radiant_q.append(radiant_idx + n)
            else:
                dire_q.append(dire_idx + n)
        return 'Radiant' if radiant_q else 'Dire'