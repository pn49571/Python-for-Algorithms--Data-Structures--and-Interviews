from collections import Counter
from collections import defaultdict

word = "ab"
string = "abxaba"

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

result = []
for i in range(len(string) - len(word) + 1):
    window = string[i:i + len(word)]
    if is_anagram(window, word):
        result.append(i)
print(result)

def del_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]

result = []
freq = defaultdict(int)

for char in word:
    freq[char] += 1

for char in string[:len(word)]:
    freq[char] -= 1
    del_if_zero(freq, char)

if not freq:
    result.append(0)

for i in range(len(word), len(string)):
    start_char, end_char = string[i - len(word)], string[i]
    freq[start_char] += 1
    del_if_zero(freq, start_char)

    freq[end_char] -= 1
    del_if_zero(freq, end_char)

    if not freq:
        beginning_index = i - len(word) + 1
        result.append(beginning_index)

print(result)