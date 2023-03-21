def reorderSpaces(text):
    num_spaces = text.count(' ')
    words = text.split()
    num_words = len(words)
    if num_words == 1:
        return words[0] + ' ' * num_spaces
    else:
        num_spaces_between_words = num_spaces // (num_words - 1)
        num_spaces_at_end = num_spaces % (num_words - 1)
        spaces_between_words = ' ' * num_spaces_between_words
        rearranged_text = spaces_between_words.join(words)
        return rearranged_text + ' ' * num_spaces_at_end