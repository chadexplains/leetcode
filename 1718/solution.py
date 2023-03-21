class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def backtrack(sequence):
            if len(sequence) == 2 * n - 1:
                return sequence
            for i in range(n, 0, -1):
                if i in used or (i > 1 and (i in used or (len(sequence) + i >= 2 * n or sequence[len(sequence) + i] != 0))):
                    continue
                used.add(i)
                sequence[len(sequence) + i] = i
                if i == 1:
                    if backtrack(sequence):
                        return sequence
                else:
                    sequence[len(sequence) - i] = i
                    if backtrack(sequence):
                        return sequence
                    sequence[len(sequence) - i] = 0
                sequence[len(sequence) + i] = 0
                used.remove(i)
            return None
        used = set()
        sequence = [0] * (2 * n - 1)
        return backtrack(sequence)