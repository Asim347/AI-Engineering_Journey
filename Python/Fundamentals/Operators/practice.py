# 1. Token Cost Estimator
total_tokens = 45000
cost_per_1000_tokens = 0.002
# Divide tokens by 1000, then multiply by the cost per 1000 tokens
total_cost = (total_tokens / 1000) * cost_per_1000_tokens
print("Total cost for processing =", total_cost)  # Added comma here!


# 2. Threshold Checker
loss_value = 0.045
if loss_value < 0.05:
    print("True")
else:
    print("False")


# 3. Deployment Gate
tests_passed = True
code_reviewed = False

is_ready = tests_passed and code_reviewed
print("Project status:", is_ready)  # Added comma here!