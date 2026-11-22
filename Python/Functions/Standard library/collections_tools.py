#The collections module provides specialized data structures that make certain tasks easier and more efficient.
# Tool	        Purpose
# Counter	        Count occurrences
# defaultdict	    Dictionary with automatic default values
# deque	        Efficient additions/removals at both ends
# namedtuple	    Tuples with named fields


from collections import Counter

reviews = ['good','bad','normal','very good','Excellent','good','bad']
word_count = Counter(reviews)
print(word_count.most_common(3))
print(word_count)

from collections import defaultdict
reviews = defaultdict(list)
reviews['positive'].append('Very good')
reviews['negative'].append('Very bad')
reviews['normal'].append(' not bad')
print(dict(reviews))

Dataset = defaultdict(list)
Dataset['positive'].append("I love this product")
Dataset['negative'].append("I don't love this product")
print(dict(Dataset))
