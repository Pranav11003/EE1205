import matplotlib.pyplot as plt
import numpy as np

# Read the generated points from the text file
data = np.loadtxt('points.txt', delimiter=',', skiprows=1)

# Extract data using NumPy array slicing
n_values = data[:, 0]
sequence_values = data[:, 1]

# Plot the graph
plt.plot(n_values, sequence_values, marker='o')
plt.title('Arithmetic Sequence: $S(n) = 12 + 4n$')
plt.xlabel('n')
plt.ylabel('S(n)')
plt.grid(True)
plt.savefig("graph1.png")
