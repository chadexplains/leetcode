class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        while i < len(code):
            if i > 0 and not stack:
                return False
            if code.startswith("<![CDATA[", i):
                j = i + 9
                i = code.find("]]>", j)
                if i < 0:
                    return False
                i += 3
            elif code.startswith("</", i):
                j = i + 2
                i = code.find(">", j)
                if i < 0 or not self.isValidTagName(code, j, i):
                    return False
                tag = code[j:i]
                if not stack or stack[-1] != tag:
                    return False
                stack.pop()
                i += 1
            elif code.startswith("<", i):
                j = i + 1
                i = code.find(">", j)
                if i < 0 or not self.isValidTagName(code, j, i):
                    return False
                tag = code[j:i]
                stack.append(tag)
                i += 1
            else:
                i += 1
        return not stack

    def isValidTagName(self, code: str, start: int, end: int) -> bool:
        if end - start < 1 or end - start > 9:
            return False
        for i in range(start, end):
            if not code[i].isupper():
                return False
        return True