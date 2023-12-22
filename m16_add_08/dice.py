import random

import matplotlib.pyplot as plt

nums = 1_000_000

sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(nums):
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    sum_counts[dice_one + dice_two] += 1

probabilities = {sum_val: count / nums for sum_val, count in sum_counts.items()}

print("Сума | Імовірність")
print("-----------------")
for sum_val, prob in probabilities.items():
    print(f"{sum_val} | {prob:.2%}")

plt.bar(probabilities.keys(), probabilities.values())
plt.xlabel("Сума")
plt.ylabel("Імовірність")
plt.show()