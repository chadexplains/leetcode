class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A.sort(reverse=True)
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                hour = str(A[i]) + str(A[j])
                if int(hour) > 23:
                    continue
                for k in range(4):
                    if k == i or k == j:
                        continue
                    minute = str(A[k]) + str(A[6-i-j-k])
                    if int(minute) > 59:
                        continue
                    return hour + ':' + minute
        return ''