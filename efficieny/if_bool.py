

# Which runs faster?
# a) random.randint(0, 1) 
# b) random.choice([True, False]) 
# c) random.random() < 0.5 



import random
import time

# Number of iterations to time
iterations = 1000000

# Timing random.randint(0, 1)
start_time = time.time()
for _ in range(iterations):
    if random.randint(0, 1):
        pass  # Just simulate the condition
end_time = time.time()
print(f"random.randint(0, 1): {end_time - start_time:.6f} seconds")

# Timing random.choice([True, False])
start_time = time.time()
for _ in range(iterations):
    if random.choice([True, False]):
        pass  # Just simulate the condition
end_time = time.time()
print(f"random.choice([True, False]): {end_time - start_time:.6f} seconds")

# Timing random.random() < 0.5
start_time = time.time()
for _ in range(iterations):
    if random.random() < 0.5:
        pass  # Just simulate the condition
end_time = time.time()
print(f"random.random() < 0.5: {end_time - start_time:.6f} seconds")
