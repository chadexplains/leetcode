class Solution:
    def toLowerCase(self, str: str) -> str:
        output = ""
        for char in str:
            if ord(char) >= 65 and ord(char) <= 90:
                output += chr(ord(char) + 32)
            else:
                output += char
        return output