import csv

# Open CSV file and read each row as a dictionary
with open("glossary.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["term"], ":", row["definition"])

        import csv
import json

valid_records = []
invalid_rows = []

# Read and validate glossary records
with open("glossary.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row_number, row in enumerate(reader, start=2):
        term = (row.get("term") or "").strip()
        definition = (row.get("definition") or "").strip()

        # Reject rows with missing fields
        if not term or not definition:
            invalid_rows.append(row_number)
            continue

        valid_records.append({
            "term": term,
            "definition": definition
        })

# Prepare summary report
report = {
    "total_valid": len(valid_records),
    "total_invalid": len(invalid_rows),
    "invalid_rows": invalid_rows,
    "records": valid_records
}

# Save report as JSON
with open("report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)

print("Report generated successfully!")