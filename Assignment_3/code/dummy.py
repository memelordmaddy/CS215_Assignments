import numpy as np

class EpanechnikovKDE:
    def __init__(self, bandwidth=1.0, sample_size=5000):
        self.bandwidth = bandwidth
        self.data = None
        self.sample_size = sample_size

    def fit(self, data):
        """Fit the KDE model with the given data."""
        if len(data) > self.sample_size:
            indices = np.random.choice(len(data), self.sample_size, replace=False)
            self.data = data[indices]
        else:
            self.data = np.array(data)

    def calculate_distances(self, points, batch_size=1000):
        """Calculate pairwise distances between points and self.data in batches."""
        n_points = len(points)
        distances = np.zeros((len(self.data), n_points))
        
        for i in range(0, n_points, batch_size):
            batch = points[i:i+batch_size]
            batch_distances = np.sqrt(((self.data[:, np.newaxis, :] - batch[np.newaxis, :, :])**2).sum(axis=2))
            distances[:, i:i+batch_size] = batch_distances
        
        return distances

    def epanechnikov_kernel(self, distances):
        """Epanechnikov kernel function."""
        scaled_distances = distances / self.bandwidth
        return np.where(scaled_distances <= 1, 
                        0.75 * (1 - scaled_distances**2) / (np.pi * self.bandwidth**2), 
                        0)

    def evaluate(self, points):
        """Evaluate the KDE at given points."""
        distances = self.calculate_distances(points)
        return np.mean(self.epanechnikov_kernel(distances), axis=0)

import numpy as np
import matplotlib.pyplot as plt

# Load the data from the NPZ file
data_file = np.load('transaction_data.npz')
data = data_file['data']

# Initialize the EpanechnikovKDE class
kde = EpanechnikovKDE(bandwidth=1.0, sample_size=5000)

# Fit the data
kde.fit(data)

# Create a grid of points (reduced resolution)
x_range = np.linspace(data[:, 0].min(), data[:, 0].max(), 50)
y_range = np.linspace(data[:, 1].min(), data[:, 1].max(), 50)
xx, yy = np.meshgrid(x_range, y_range)
grid_points = np.column_stack([xx.ravel(), yy.ravel()])

# Evaluate KDE on the grid
z = kde.evaluate(grid_points).reshape(xx.shape)

# Plot the estimated density in a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xx, yy, z, cmap='viridis', edgecolor='none')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Density')
ax.set_title('2D Epanechnikov Kernel Density Estimation')
fig.colorbar(surf, shrink=0.5, aspect=5)

# Save the plot
plt.savefig('2d_epanechnikov_kde_plot.png')
plt.show()

# Create a 2D contour plot
plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, z, levels=20, cmap='viridis')
plt.colorbar(label='Density')
plt.scatter(data[:, 0], data[:, 1], alpha=0.1, color='red', s=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Epanechnikov KDE Contour Plot')
plt.savefig('2d_epanechnikov_kde_contour.png')
plt.show()