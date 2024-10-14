import numpy as np
import matplotlib.pyplot as plt

# Custom Epanechnikov KDE class
class EpanechnikovKDE:
    def __init__(self, bandwidth=1.0):
        self.bandwidth = bandwidth
        self.data = None

    def fit(self, data):
        """Fit the KDE model with the given data."""
        self.data= np.array(data)

    def epanechnikov_kernel(self, x, xi):
        """Epanechnikov kernel function."""
        y= (x-xi)/self.bandwidth
        if(np.abs(y)<=1):
            return 0.75 * (1-y**2)/ self.bandwidth
        else:
            return 0

    def evaluate(self, x):
        """Evaluate the KDE at point x."""
        x = np.array(x)[:, np.newaxis]  # Add a new axis to x
        return np.mean(self.epanechnikov_kernel(x, self.data), axis=1)


# Load the data from the NPZ file
data_file = np.load('transaction_data.npz')
data = data_file['data']
print(data.shape)

# TODO: Initialize the EpanechnikovKDE class
kde = EpanechnikovKDE(bandwidth=1.0)

# TODO: Fit the data
kde.fit(data)

# TODO: Plot the estimated density in a 3D plot
# TODO: Save the plot 
x_k= np.linspace(data.min(), data.max(), 1000)
y_k= kde.evaluate(x_k)
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black')
plt.plot(x_k, y_k, 'r-', lw=2)
plt.title('Epanechnikov Kernel Density Estimation')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(True, alpha=0.3)
plt.show()