
def filter(word_list, n):
    return [word for word in word_list if len(word) > n]

words = ["apple", "banana", "grape", "kiwi", "orange"]
n = 4
a = filter(words, n)
print(a)
