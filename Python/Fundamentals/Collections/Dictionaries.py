# A dictionary is a mutable collection that stores data in key-value pairs.
# Unlike lists and tuples, dictionaries use keys to access values instead of numerical indexes.

student = {
    "name": "Asim",
    "age": 21,
    "course": "Computer Science"
}

print(student)
print(type(student))

student = {
    'name' : 'Asim',
    'age' : 21,
    'Course' : 'Computer Science'
}
print(student['name'])
print(student['age'])

print(student.get("email", "Not available"))


student = {
    "name": "Asim",
    "age": 21,
    "course": "Python"
}
print(student.keys())
print(student.values())
print(student.items())


student = {
    "name": "Asim",
    "age": 21,
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)