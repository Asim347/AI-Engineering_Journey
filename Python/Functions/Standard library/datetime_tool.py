# The datetime module handles dates, times, timestamps and date calculations.

# Common uses:
# - Recording when users make API requests.
# - Tracking model training duration.
# - Creating timestamps for datasets.
# - Measuring processing time.

from datetime import datetime

now = datetime.now()
format = now.strftime("%d-%m-%Y %H:%M:%S")
print(now)
print(format)

#Task 2

start_time = datetime.now()
print("Training time of a model...")

end_time = datetime.now()

training_time = end_time = start_time

print("Training time is now",training_time)