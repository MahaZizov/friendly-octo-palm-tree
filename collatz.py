import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def collatz(num):
    num_list = []
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            num_list.append(num)
        else:
            num = num * 3 + 1
            num_list.append(num)
    return num_list


rng = np.random.default_rng()
digits = rng.integers(1500, 2500, size=10)
two_digits = rng.integers(2500, 3500, size=10)
three_digits = rng.integers(3500, 4500, size=10)
four_digits = rng.integers(1000, 2000, size=10)

sample1 = np.random.choice(digits, size=1)
sample2 = np.random.choice(two_digits, size=1)
sample3 = np.random.choice(three_digits, size=1)
sample4 = np.random.choice(four_digits, size=1)

num1 = sample1.item()
num2 = sample2.item()
num3 = sample3.item()
num4 = sample4.item()

df1 = pd.DataFrame(collatz(num1))
df2 = pd.DataFrame(collatz(num2))
df3 = pd.DataFrame(collatz(num3))
df4 = pd.DataFrame(collatz(num4))


fig, ax = plt.subplots()
ax.plot(df1)
ax.plot(df2)
ax.plot(df3)
ax.plot(df4)
ax.legend([num1, num2, num3, num4])
plt.show()
