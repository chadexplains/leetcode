class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [collections.defaultdict(int)]
        i = 0
        while i < len(formula):
            if formula[i] == '(': # start of nested formula
                stack.append(collections.defaultdict(int))
                i += 1
            elif formula[i] == ')': # end of nested formula
                counts = stack.pop()
                i += 1
                j = i
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                factor = int(formula[i:j] or 1)
                for element, count in counts.items():
                    stack[-1][element] += count * factor
                i = j
            else: # start of new element
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1
                element = formula[i:j]
                i = j
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                count = int(formula[i:j] or 1)
                stack[-1][element] += count
                i = j
        counts = stack.pop()
        return ''.join(element + (str(counts[element]) if counts[element] > 1 else '') for element in sorted(counts))