def translate(text):
    vowels = "aeiou"
    translated_words = []

    for word in text.split():
        if word[0] in vowels or word.startswith(("xr", "yt")):
            translated_words.append(word + "ay")
            continue

        # Find "qu" after zero or more consonants.
        qu_index = word.find("qu")

        if qu_index != -1 and all(
            letter not in vowels for letter in word[:qu_index]
        ):
            split_index = qu_index + 2
        else:
            # Find the first vowel or y after a consonant.
            split_index = next(
                index
                for index, letter in enumerate(word)
                if letter in vowels or (letter == "y" and index > 0)
            )

        translated_words.append(
            word[split_index:] + word[:split_index] + "ay"
        )

    return " ".join(translated_words)
