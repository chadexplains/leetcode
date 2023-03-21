class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        min_val, max_val = 0, len(S)
        output = []
        for char in S:
            if char == 'I':
                output.append(min_val)
                min_val += 1
            else:
                output.append(max_val)
                max_val -= 1
        output.append(min_val)
        return output