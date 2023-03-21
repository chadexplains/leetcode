class Solution:
    def entityParser(self, text: str) -> str:
        html_entities = {
            '&quot;': '"',
            '&apos;': "'",
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/'
        }
        i = 0
        result = ''
        while i < len(text):
            if text[i] == '&':
                j = i + 1
                while j < len(text) and text[j] != ';':
                    j += 1
                if j < len(text) and text[i:j+1] in html_entities:
                    result += html_entities[text[i:j+1]]
                    i = j + 1
                    continue
            result += text[i]
            i += 1
        return result