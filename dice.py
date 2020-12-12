# Import numpy as np
import numpy as np

np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))

dice_outcome = []


for toss in range(0, 50):
    dice_throw = np.random.randint(1,7)
    dice_outcome.append(dice_throw)


print(dice_outcome)