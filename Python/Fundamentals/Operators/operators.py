# ==========================================
# 1. ARITHMETIC OPERATORS (Math calculations)
# ==========================================
total_tokens = 1500
tokens_per_batch = 32

# Division / Floor Division / Modulus
full_batches = total_tokens // tokens_per_batch  # Integer division (drops remainder)
leftover_tokens = total_tokens % tokens_per_batch   # Remainder after grouping
exponent_calc = 2 ** 3                             # Exponentiation (2 raised to power 3)

print("--- Arithmetic Operators ---")
print(f"Full Batches: {full_batches}, Leftover: {leftover_tokens}, Exponent: {exponent_calc}")


# ==========================================
# 2. COMPARISON OPERATORS (Returns True/False)
# ==========================================
required_accuracy = 0.90
model_accuracy = 0.92

print("\n--- Comparison Operators ---")
print("Is accuracy met?", model_accuracy >= required_accuracy)
print("Is accuracy different from requirement?", model_accuracy != required_accuracy)


# ==========================================
# 3. LOGICAL OPERATORS (combine conditions)
# ==========================================
has_gpu = True
is_memory_sufficient = False

print("\n--- Logical Operators ---")
# 'and' requires BOTH to be True
print("Ready to train (and):", has_gpu and is_memory_sufficient)  # False

# 'or' requires AT LEAST ONE to be True
print("Ready to train (or):", has_gpu or is_memory_sufficient)   # True

# 'not' inverts the boolean value
print("Inverted GPU status (not):", not has_gpu)                 # False


# ==========================================
# 4. ASSIGNMENT OPERATORS (update in-place)
# ==========================================
print("\n--- Assignment Operators ---")
total_epochs = 10
print("Initial epochs:", total_epochs)

total_epochs += 5  # Equivalent to: total_epochs = total_epochs + 5
print("Epochs after += 5:", total_epochs)