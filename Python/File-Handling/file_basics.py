# Write data into a file
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("AI Engineering Journey")

# Read the saved data
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


    from pathlib import Path

# Create a path for the file
file_path = Path("ai_notes.txt")

# Add new content without deleting existing content
with file_path.open("a", encoding="utf-8") as file:
    file.write("\nLearning Python file handling")

# Check whether the file exists
if file_path.exists():
    print("File exists!")
    print(file_path.read_text(encoding="utf-8"))