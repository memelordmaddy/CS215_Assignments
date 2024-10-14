import numpy as np
import matplotlib.pyplot as plt

class EpanechnikovKDE:
    def __init__(self, bandwidth=1.0):
        self.bandwidth = bandwidth
        self.data = None

    def fit(self, data):
        """Fit the KDE model with the given data."""
        self.data = np.array(data)

    def epanechnikov_kernel(self, x, xi):
        """Epanechnikov kernel function."""
        distances_squared = np.sum(((x - xi) / self.bandwidth)**2, axis=1)
        condition = distances_squared <= 1
        return (2 / np.pi) * (1 - distances_squared) * condition

    def evaluate(self, x):
        """Evaluate the KDE at multiple points x."""
        return np.sum(self.epanechnikov_kernel(x, self.data)) / (len(self.data) * self.bandwidth**2)


# Load the data from the NPZ file
data_file = np.load('transaction_data.npz')
data = data_file['data']
print(data.shape)

bandwidth = 1.0  # You may need to adjust this value
kde = EpanechnikovKDE(bandwidth=bandwidth)

# Fit the data
kde.fit(data)
# Define the range for evaluation
x_min, x_max = data[:, 0].min(), data[:, 0].max()
y_min, y_max = data[:, 1].min(), data[:, 1].max()

# Create a grid of points
x = np.linspace(x_min, x_max, 100)
y = np.linspace(y_min, y_max, 100)
X, Y = np.meshgrid(x, y)
grid_points = np.c_[X.ravel(), Y.ravel()]

# Evaluate KDE on the grid (vectorized)
Z = np.array([kde.evaluate(point) for point in grid_points]).reshape(X.shape)

# Create a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Add labels and title
ax.set_title('3D Probability Density of Transactions')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Density')

# Save the plot
plt.savefig('transaction_distribution_3d.png')
plt.show()
