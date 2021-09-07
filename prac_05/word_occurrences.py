"""Word Occurrences"""

words_from_text = {}

text = input("Text: ").split()

for word in text:
    if word in words_from_text:
        words_from_text[word] += 1
    else:
        words_from_text[word] = 1

words = list(words_from_text.keys())
words.sort()

largest_word = max([len(word) for word in words])
for word in words:
    print(f'{word:{largest_word}} : {words_from_text[word]}')

print("Hello World")
