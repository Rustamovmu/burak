# TASK L

# So'zlarni ketma-ketligini buzmasdan har bir so'zni alohida teskarisiga o'girib beradigan function tuzing.

# Masalan: reverseSentence("we like coding!") return "ew ekil !gnidoc"


def reverseSentence(sentence):
    words = sentence.split()
    reverse_words = []

    for word in words:
        reverse_words.append(word[::-1])

    return " ".join(reverse_words)


print(reverseSentence("we like coding!"))
