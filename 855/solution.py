class ExamRoom:
    def __init__(self, N: int):
        self.N = N
        self.students = []

    def seat(self) -> int:
        if not self.students:
            student = 0
        else:
            max_dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    dist = (s - prev)//2
                    if dist > max_dist:
                        max_dist, student = dist, prev+dist
            dist = self.N - 1 - self.students[-1]
            if dist > max_dist:
                student = self.N - 1
        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)

