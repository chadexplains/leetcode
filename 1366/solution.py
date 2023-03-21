class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        rank = [[0] * 26 + [chr(i)] for i in range(65, 91)]
        for vote in votes:
            for i, team in enumerate(vote):
                rank[ord(team) - 65][i] -= 1
        rank.sort()
        return ''.join([c for _, _, c in rank if c != '\0'])