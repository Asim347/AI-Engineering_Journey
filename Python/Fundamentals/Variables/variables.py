# 1. Create 10 variables representing an AI engineering project
project_name = "NeuralNetX"
model_version = 1.0
learning_rate = 0.001
batch_size = 32
epochs = 50
is_training = True
optimizer = "Adam"
loss_function = "CrossEntropy"
dataset_size = 50000
gpu_accelerated = True

# 2. Reassign values to three variables
model_version = 1.1
batch_size = 64
epochs = 100

# 3. Assign the same value to multiple variables
train_status = val_status = test_status = "Pending"

# 4. Explore id() and type()
print("--- Variables Exploration ---")
print("Type of learning_rate:", type(learning_rate))
print("Memory ID of learning_rate:", id(learning_rate))