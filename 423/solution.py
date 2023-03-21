class Solution:
    def originalDigits(self, s: str) -> str:
        digit_to_letter = {"0": "z", "1": "o", "2": "w", "3": "h", "4": "u", "5": "f", "6": "x", "7": "s", "8": "g", "9": "i"}
        digit_to_letters = {"0": set("zero"), "1": set("one"), "2": set("two"), "3": set("three"), "4": set("four"), "5": set("five"), "6": set("six"), "7": set("seven"), "8": set("eight"), "9": set("nine")}
        letter_counts = collections.Counter(s)
        digit_counts = collections.Counter()
        for digit in "02468":
            letter = digit_to_letter[digit]
            count = letter_counts[letter]
            digit_counts[digit] += count
            for letter in digit_to_letters[digit]:
                letter_counts[letter] -= count
        for digit in "13579":
            letter = next(iter(digit_to_letters[digit]))
            count = letter_counts[letter]
            digit_counts[digit] += count
            for letter in digit_to_letters[digit]:
                letter_counts[letter] -= count
        return ''.join(digit * digit_counts[digit] for digit in "0123456789")