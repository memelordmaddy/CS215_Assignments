import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def sample(loc, scale, size=100000):
    sample_input = np.random.uniform(0, 1, size)
    sample_output = norm.ppf(sample_input, loc=loc, scale=scale)
    return sample_output

parameters = [(0, 0.2), (0, 1.0), (0, 5.0), (-2, 0.5)]
samples = [sample(loc, scale) for loc, scale in parameters]

plt.figure(figsize=(8, 8))

colors = ['blue', 'red', 'yellow', 'green']
labels = [r'$\mu = 0, \sigma^2 = 0.2$', 
          r'$\mu = 0, \sigma^2 = 1.0$', 
          r'$\mu = 0, \sigma^2 = 5.0$', 
          r'$\mu = -2, \sigma^2 = 0.5$']

figure_number = 1
for loc, scale in parameters:
    plt.hist(samples[figure_number-1], bins=200, density=True, alpha=0.5, color=colors[figure_number-1], label=labels[figure_number-1])
    figure_number += 1

plt.title("Gaussian Distribution with different parameters.")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.legend(loc="upper right")

plt.tight_layout()
plt.savefig('2c.png')
plt.show()