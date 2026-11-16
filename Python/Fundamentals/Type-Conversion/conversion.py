# ==========================================
# 1. IMPLICIT CONVERSION (Automatic by Python)
# ==========================================
epochs = 10         # int
learning_rate = 0.05  # float

result = epochs + learning_rate  # int + float automatically becomes float
print("--- Implicit Conversion ---")
print(f"Result: {result} | Type: {type(result)}")


# ==========================================
# 2. EXPLICIT CONVERSION (Type Casting)
# ==========================================
# Simulating a user input string representing a batch size
user_input_batch = "64" 
print("\n--- Explicit Conversion ---")
print("Original input type:", type(user_input_batch))

# Convert string to integer for math operations
actual_batch_size = int(user_input_batch)
print("Converted batch size type:", type(actual_batch_size))

# Converting float to int (drops the decimal part / precision loss)
exact_loss = 0.099
rounded_down_loss = int(exact_loss)
print(f"Original float: {exact_loss} | Cast to int: {rounded_down_loss}")