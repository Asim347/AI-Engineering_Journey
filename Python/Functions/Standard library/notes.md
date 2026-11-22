# Python Standard Library — Notes

## 1. Collections
- `Counter`: Counts occurrences of elements.
- `defaultdict`: Provides default values for missing keys.
- `deque`: Efficient insertion and removal from both ends.

## 2. Itertools
- `chain()`: Combines multiple iterables.
- `combinations()`: Generates groups where order doesn't matter.
- `permutations()`: Generates arrangements where order matters.
- `islice()`: Extracts a portion of an iterator.

## 3. Regular Expressions (`re`)
- `re.search()`: Searches for a pattern.
- `re.findall()`: Finds all matches.
- `re.sub()`: Replaces matching patterns.
- `re.split()`: Splits text using a pattern.

Common patterns:
- `\d` — Digits
- `\w` — Word characters
- `\s` — Whitespace
- `+` — One or more
- `*` — Zero or more
- `^` — Start of string
- `$` — End of string

## 4. Datetime
- `datetime.now()`: Gets current date and time.
- `strftime()`: Converts datetime into formatted text.
- `strptime()`: Converts text into datetime.
- `timedelta`: Performs date and time calculations.

## 5. Random
- `random()`: Generates a random decimal.
- `randint()`: Generates a random integer.
- `choice()`: Selects one random element.
- `sample()`: Selects unique random elements.
- `shuffle()`: Shuffles a list.

`random.seed(42)` helps reproduce random results.

## Real-world AI Engineering Applications
- Collections: Dataset frequency counting and grouping.
- Itertools: Generating experimental combinations.
- Regex: Cleaning and preprocessing text.
- Datetime: Recording training and experiment timestamps.
- Random: Dataset sampling and reproducible experiments.

## Important
Avoid naming Python files after standard library modules, such as `collections.py`, `random.py`, or `datetime.py`, to prevent import conflicts.