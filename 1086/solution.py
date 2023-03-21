class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = {}
        for item in items:
            if item[0] not in scores:
                scores[item[0]] = []
            scores[item[0]].append(item[1])
        result = []
        for student in scores:
            scores[student].sort(reverse=True)
            avg = sum(scores[student][:5]) // 5
            result.append([student, avg])
        return result