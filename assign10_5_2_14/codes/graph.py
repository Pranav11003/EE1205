import matplotlib.pyplot as plt
import numpy as np

# Load the generated points from the text file using numpy
file_path = 'points.txt'
data = np.loadtxt(file_path, delimiter=',', skiprows=1)

# Extract n and S(n) from the data
n_values = data[:, 0].astype(int)
sequence_values = data[:, 1].astype(int)

# Plot the stem graph
plt.stem(n_values, sequence_values, basefmt='b-', linefmt='r-', markerfmt='ro')
plt.xlabel('n')
plt.ylabel('X(n)')
plt.grid(True)
plt.savefig("graph1.png")
