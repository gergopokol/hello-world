from collections import Counter

def word_count_distribution(text):
    word_counts = count_words_fast(text)
    count_distribution = Counter(word_counts.values())
    return count_distribution

distribution = word_count_distribution(text)