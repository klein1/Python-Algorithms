from collections import Counter

words = [
    'look', 'into', 'AAA', 'cdf', 'my', 'AAA',
    'the', 'AAA', 'into', 'the', 'my', 'MY',
    'BBB', 'AAA', 'look', 'BBB', 'not', 'the',
    'AAA','into', 'CCC','the'
]
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)