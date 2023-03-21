class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        letter_to_morse = {chr(i + 97): morse_code[i] for i in range(26)}
        transformations = set()
        for word in words:
            transformation = ""
            for letter in word:
                transformation += letter_to_morse[letter]
            transformations.add(transformation)
        return len(transformations)