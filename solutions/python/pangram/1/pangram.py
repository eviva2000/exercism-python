
def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(sentence.lower())