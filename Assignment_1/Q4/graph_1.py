import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 1 / (x - 1)
m = 2  
n = 10  
x = np.linspace(m + 1, n + 1, 1000)
plt.plot(x, f(x), label=r'$f(x) = \frac{1}{x-1}$')
bins = np.arange(m + 1, n + 2, 1)
for b in bins:
    plt.axvline(x=b, color='gray', linestyle='--', linewidth=0.5)
for i in range(m + 1, n + 1):
    x_left = i
    height = f(x_left)  
    plt.bar(x_left, height, width=1, align='edge', color='orange', alpha=0.5, edgecolor='black')
xticks = list(range(m + 1, n + 2)) 
xtick_labels = ["m+1", "m+2", ".", ".", ".", ".", ".", ".", "n+1"]  
plt.xticks(xticks, xtick_labels)
plt.yticks([])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
