# Regular expressions (Regex) are patterns used to search, match, extract, replace or validate text.
# Why is Regex important?

# AI applications frequently receive messy text:
# - Extra spaces.
# - Unwanted symbols.
# - Emails and phone numbers.
# - HTML tags.
# - Inconsistent formatting.
# The re module helps process this text before further analysis.

import re
text = "Contact us one adim@gmail.com or support@gmail.com"
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

print(emails)

import re

text = "Hello!!! Python @@@ AI ####"
# Replace characters other than letters, digits and spaces
cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
print(cleaned)


#Task 3

def clean_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    # Remove unwanted punctuation
    text = re.sub(r'[^a-z0-9\s]', '', text)

    # Normalize multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


review = "GREAT PRODUCT!!! Visit https://example.com"

print(clean_text(review))