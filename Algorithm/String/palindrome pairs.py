words = ["code", "edoc", "da", "d"]
def is_palindrome(word):
    return word == word[::-1]

result = []
for i, word1 in enumerate(words):
    for j, word2 in enumerate(words):
        if i == j:
            continue
        if is_palindrome(word1+word2):
            result.append((i, j))

print(result)