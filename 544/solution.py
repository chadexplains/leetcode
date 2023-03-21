def findContestMatch(n):
    teams = [i for i in range(1, n+1)]
    def helper(teams):
        if len(teams) == 1:
            return str(teams[0])
        matches = []
        for t1, t2 in zip(teams[:len(teams)//2], teams[len(teams)//2:][::-1]):
            matches.append('('+str(t1)+','+str(t2)+')')
        return helper(matches)
    return helper(teams)