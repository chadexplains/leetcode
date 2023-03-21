def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        s = sum(digits)
        if s == 0:
            return "0"
        if s % 3 == 0:
            return ''.join(map(str, digits))
        else:
            r1, r2 = [], []
            for d in digits:
                if d % 3 == 1:
                    r1.append(d)
                elif d % 3 == 2:
                    r2.append(d)
            r1.sort()
            r2.sort()
            if s % 3 == 1:
                if len(r1) >= 1:
                    digits.remove(r1[0])
                else:
                    digits.remove(r2[0])
                    digits.remove(r2[1])
            else:
                if len(r2) >= 1:
                    digits.remove(r2[0])
                else:
                    digits.remove(r1[0])
                    digits.remove(r1[1])
            if len(digits) == 0:
                return ""
            digits.sort(reverse=True)
            return ''.join(map(str, digits))