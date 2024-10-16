import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pass the path to data.csv 
df = pd.read_csv('data.csv', usecols=[6], nrows=1500, header=13)

data = df.iloc[:, 0].to_numpy()
data = data[data <= 4]

counts = plt.hist(data, bins=np.linspace(0, 4, 11))[0]
plt.title("Filtered data")
plt.xlabel("Reading")
plt.ylabel("Number of readings")
plt.savefig("10binhistogram.png")

total_count = np.sum(counts)
probability = counts / total_count

print("Data distribution")
print(probability)

def cross_validation_score(data, n):
    nbins = np.arange(1, 1001)
    h = 4 / nbins
    counts = np.zeros((len(nbins), nbins[-1]))

    for idx, nb in enumerate(nbins):
        counts[idx, :nb] = np.histogram(data, np.linspace(0, 4, nb + 1))[0]

    probabilities = counts / n
    pj_2 = np.sum(probabilities ** 2, axis=1)
    y_h = (2 / ((n - 1) * h)) - ((n + 1) * pj_2) / ((n - 1) * h)

    plt.clf()
    plt.plot(h, y_h)
    plt.title("Cross Validation Score Vs Bandwidth")
    plt.ylabel("Cross Validation Score")
    plt.xlabel("Bandwidth(h)")
    plt.savefig("crossvalidation.png")

    h_min = h[np.argmin(y_h)]
    
    return h_min

h_min = cross_validation_score(data, total_count)
print("Optimal bandwidth :", h_min)

plt.clf()
counts = plt.hist(data, bins=np.linspace(0, 4, int(4/h_min)+1))[0]
plt.title("Optimal Histogram")
plt.ylabel("Frequency")
plt.xlabel("Reading")
plt.savefig("optimalhistogram.png")
