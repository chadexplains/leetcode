class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbreviations = {}
        for word in dictionary:
            abbreviation = self.get_abbreviation(word)
            if abbreviation in self.abbreviations:
                if self.abbreviations[abbreviation] != word:
                    self.abbreviations[abbreviation] = None
            else:
                self.abbreviations[abbreviation] = word

    def isUnique(self, word: str) -> bool:
        abbreviation = self.get_abbreviation(word)
        if abbreviation not in self.abbreviations:
            return True
        elif self.abbreviations[abbreviation] == word:
            return True
        else:
            return False

    def get_abbreviation(self, word: str) -> str:
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]
