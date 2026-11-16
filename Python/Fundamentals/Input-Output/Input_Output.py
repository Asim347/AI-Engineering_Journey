# ==========================================
# 1. GETTING USER INPUT
# ==========================================
# Note: input() always returns a string
username = input("Enter your name: ")
print(f"Hello, {username}! Welcome to your AI engineering journey.")


# ==========================================
# 2. CUSTOM PRINT FORMATTING (sep and end)
# ==========================================
# Using 'sep' to change what goes between items
print("Python", "Pandas", "PyTorch", sep=" -> ")

# Using 'end' to change what happens at the very end of the print statement
print("Loading model...", end=" ")
print("Done!")