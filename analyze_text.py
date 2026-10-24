
def analyze_text(text: str, target_word: str):

    words = text.split()
    word_count = len(words)

    target_count = 0

    for word in words:
        if word.lower() == target_word.lower():
            target_count += 1

    if words:
        longest_word = max(words, key=len)
    else:
        longest_word = ""

    return word_count, target_count, longest_word

#text და target_word:
print(analyze_text("Python is great and python is easy", "python"))

