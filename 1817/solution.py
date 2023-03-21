class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[List[int]]:
        user_minutes = defaultdict(set)
        for user, minute in logs:
            user_minutes[user].add(minute)
        result = [0] * k
        for user, minutes in user_minutes.items():
            result[len(minutes) - 1] += 1
        return [[i + 1, result[i]] for i in range(k)]
}