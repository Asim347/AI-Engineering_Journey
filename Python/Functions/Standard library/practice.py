# AI Dataset Word Counter
# Use collections.Counter.
# Requirements:
# - Create a list containing words extracted from AI-related text.
# - Count how many times each word appears.
# - Display the three most common words.

print("---------------1-------------")
from collections import Counter

words = ['Data','LLMS','Agents','Algorithms','Models','Data','RAG','Python','Models','Data','RAG','Deep learning']
counted_words = Counter(words)
print(counted_words)
print(counted_words.most_common(3))


print("---------------2-------------")
#2 AI Dataset Sampling
# Use itertools and random.
# Requirements:
# - Create two lists of AI training samples.
# - Combine them using chain().
# - Randomly select five samples.
# - Print the selected samples

from itertools import chain
import random

list1 = ['Pakistan','is','a','beautiful','city']
list2 = ['it','is','situated','in a','Asia']

combined = chain(list1,list2)
random_picks = random.sample(list2,5)
print(random_picks)
print(list(combined))

#Task 3
# Use re and collections.

# Requirements:
# - Create a list of five messy customer reviews.
# - Convert text to lowercase.
# - Remove URLs.
# - Remove unnecessary special characters.
# - Normalize multiple spaces.
# - Count the most frequent words using Counter.

print("---------------3-------------")

import re
from collections import Counter

# Step 1: Create a list of five messy customer reviews
reviews = [
    'I   @@@ writing THIS',
    'We Are haViiig Party !!!',
    'This is GOoD modEl',
    'I LIIKe YOU',
    'HOW ARE YOU',
]

cleaned_reviews = []
all_words = []

for review in reviews:
    # Step 2: Convert text to lowercase
    text = review.lower()

    # Step 3: Remove URLs (matches http://, https://, or www. links)
    text = re.sub(r'(https?://\S+|www\.\S+)', '', text)

    # Step 4: Remove unnecessary special characters (keep only lowercase letters, digits, and spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)

    # Step 5: Normalize multiple spaces into a single space and trim outer spaces
    text = re.sub(r'\s+', ' ', text).strip()

    cleaned_reviews.append(text)

    # Split cleaned text into individual words and collect them
    if text:
        all_words.extend(text.split())

# Step 6: Count word frequencies using Counter
word_counts = Counter(all_words)

print('Cleaned Reviews:')
for item in cleaned_reviews:
    print(' -', item)

print('\nMost Frequent Words:')
for word, count in word_counts.most_common():
    print(f'  {word}: {count}')
