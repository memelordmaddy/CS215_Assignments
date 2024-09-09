import numpy as np
import matplotlib.pyplot as plt

def galton_board(h, N):
    moves = np.random.choice([-1,1], (N,h))
    pockets = np.sum(moves, axis=1)
    return pockets

depths = [10, 50, 100]
N = 100000

for h in depths:
    pockets = galton_board(h, N)

    unique, counts = np.unique(pockets, return_counts=True)

    plt.figure(figsize=(10, 6))
    plt.bar(unique, counts, color='blue', alpha=0.7)
    plt.title(f"Galton Board Simulation with h = {h} and N = {N}")
    plt.xlabel("Pocket")
    plt.ylabel("Number of Balls")
    plt.savefig(f'2d{depths.index(h)+1}.png')
    plt.show()
