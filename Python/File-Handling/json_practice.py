import json

# Python dictionary containing model configuration
model_config = {
    "model": "GPT",
    "temperature": 0.7,
    "max_tokens": 1000
}

# Save dictionary into a JSON file
with open("config.json", "w", encoding="utf-8") as file:
    json.dump(model_config, file, indent=4)

# Read JSON file back into Python
with open("config.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
print(data["model"])



import json

# Python dictionary
student = {"name": "Asim", "field": "AI Engineering"}

# Convert dictionary into JSON string
json_string = json.dumps(student, indent=4)
print(json_string)

# Convert JSON string back into Python dictionary
python_data = json.loads(json_string)
print(python_data["field"])