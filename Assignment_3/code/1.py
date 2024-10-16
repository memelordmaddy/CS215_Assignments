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

    x = []
    y = []
    for nbins in range(1, 1001):
        h = 4 / nbins

        _bins = np.linspace(0, 4, nbins + 1)
        count = np.histogram(data, _bins)[0]
        probability = (count / n)

        pj_2 = np.sum(probability ** 2)

        y_h = 2/((n - 1) * h) - ((n + 1) * pj_2)/((n - 1) * h)
        x.append(h)
        y.append(y_h)

    plt.clf()
    plt.plot(x, y)
    plt.title("Cross Validation Score Vs Bandwidth")
    plt.ylabel("Cross Validation Score")
    plt.xlabel("Bandwidth(h)")
    plt.savefig("crossvalidation.png")

    h_min = x[np.argmin(y)]
    
    return h_min

h_min = cross_validation_score(data, total_count)
print("Optimal bandwidth :", h_min)

plt.clf()
counts = plt.hist(data, bins=np.linspace(0, 4, int(4/h_min)+1))[0]
plt.title("Optimal Histogram")
plt.ylabel("Frequency")
plt.xlabel("Reading")
plt.savefig("optimalhistogram.png")
