
def filter_long_words(word_list, n):
    return [word for word in word_list if len(word) > n]

words = ["apple", "banana", "grape", "kiwi", "orange"]
n = 4
filtered_words = filter_long_words(words, n)
print("Words longer than {} characters:".format(n), filtered_words)
