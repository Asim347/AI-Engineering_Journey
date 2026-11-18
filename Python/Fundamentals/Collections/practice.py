# Task 1 — Lists
# Create a list of five book titles.
# - Print the first and last books.
# - Add another book.
# - Remove one book.
# - Sort the list alphabetically.
# - Print the final list.

books_list = ['alchemist','ai','science','math','english']
print(books_list[0])
print(books_list[-1])

books_list.append("urdu")
print(books_list)

books_list.remove('ai')

books_list.sort(reverse=False)

print(books_list)

# Task 2 — Tuples
# Create a tuple containing five programming languages.
# - Print the first and last elements.
# - Find the length.
# - Count how many times "Python" appears.
# - Try changing one element and observe what happens.

print("----------- Task 2 ------------")
programming_languages = ('C','C++','Python','Java','Rust')
print(programming_languages[0])
print(programming_languages[-1])

print(len(programming_languages))

print(programming_languages.count('python'))

programming_languages['0'] == 'Javascript'



print("----------- Task 3 ------------")


# Task 3 — Dictionaries
# Create a student dictionary containing:
# name = "Asim"age = 21course = "Computer Science"

# - Print the student's name.
# - Add a "university" key.
# - Update the age.
# - Print all key-value pairs using a loop.

student = {
    "name": "Asim",
    "age": 21,
    "course": "Computer Science"
}

# Access
print(student["name"])

# Add university
student["university"] = "Your University"

# Update age
student["age"] = 22

# Display all key-value pairs
for key, value in student.items():
    print(key, ":", value)
