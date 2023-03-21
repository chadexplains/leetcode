class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pref = {}
        for i in range(n):
            pref[i] = preferences[i]
        pair_dict = {}
        for pair in pairs:
            pair_dict[pair[0]] = pair[1]
            pair_dict[pair[1]] = pair[0]
        unhappy = 0
        for i in range(n):
            for j in range(n):
                if i != j and pref[i].index(j) < pref[i].index(pair_dict[i]) and pref[j].index(i) < pref[j].index(pair_dict[j]):
                    unhappy += 1
                    break
        return unhappy