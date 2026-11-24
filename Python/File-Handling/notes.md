# Files, JSON and CSV — Notes

## 1. File Handling
- `open()` — Opens a file.
- `read()` — Reads file content.
- `write()` — Writes content (overwrites existing content in `"w"` mode).
- `append` (`"a"`) — Adds content without removing existing data.
- `with open()` — Automatically closes files.
- `pathlib` — Provides an easy way to work with file paths.
- `encoding="utf-8"` — Supports text from different languages.

## 2. JSON
JSON (JavaScript Object Notation) stores structured data using key-value pairs.

| Function | Purpose |
|---|---|
| `json.dump()` | Writes Python data into a JSON file |
| `json.load()` | Reads data from a JSON file |
| `json.dumps()` | Converts Python data into a JSON string |
| `json.loads()` | Converts JSON string into Python data |

**AI Use:** Store model configurations, API responses, and structured data.

## 3. CSV
CSV (Comma-Separated Values) stores data in rows and columns.

| Function | Purpose |
|---|---|
| `csv.reader()` | Reads rows as lists |
| `csv.DictReader()` | Reads rows as dictionaries |
| `csv.writer()` | Writes rows |
| `csv.DictWriter()` | Writes dictionaries as rows |

**AI Use:** Load datasets, validate records, and prepare training data.

## 4. Important Concepts
- Validate data before processing.
- Use `.strip()` to remove extra spaces.
- Handle missing values.
- Use `try/except` for file errors.
- Use JSON for structured reports.
- Use CSV for tabular datasets.

## 5. Mini Project — CSV Glossary Loader

**Goal:** Read AI/ML terms from a CSV file, validate records, and generate a JSON report.

Steps:
1. Read `glossary.csv`.
2. Validate terms and definitions.
3. Separate valid and invalid records.
4. Count invalid rows.
5. Save the results in `report.json`.

## 6. Learning Structure

Every Python lesson file contains:
- Two solved code examples with explanatory comments.
- One medium-level practice question.
- AI Engineering-related examples and applications.

Practice questions should be attempted independently before reviewing solutions.

## 7. File Structure

```text
File-Handling/
├── file_basics.py
├── json_practice.py
├── csv_glossary_loader.py
├── glossary.csv
├── report.json
└── notes.md
```

**Lesson 10 Status:** Files, JSON and CSV — Completed after finishing the practice tasks and mini-project.
