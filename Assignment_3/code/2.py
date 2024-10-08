import numpy as np
import matplotlib.pyplot as plt

# Custom Epanechnikov KDE class
class EpanechnikovKDE:
    def __init__(self, bandwidth=1.0):
        self.bandwidth = bandwidth
        self.data = None

    def fit(self, data):
        """Fit the KDE model with the given data."""
        TODO

    def epanechnikov_kernel(self, x, xi):
        """Epanechnikov kernel function."""
        TODO

    def evaluate(self, x):
        """Evaluate the KDE at point x."""
        TODO


# Load the data from the NPZ file
data_file = np.load('transaction_data.npz')
data = data_file['data']

# TODO: Initialize the EpanechnikovKDE class

# TODO: Fit the data

# TODO: Plot the estimated density in a 3D plot

# TODO: Save the plot 