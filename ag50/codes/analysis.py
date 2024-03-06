import matplotlib.pyplot as plt
import numpy as np

# Function to read data from a file and return two lists (x and y values)
def read_data(file_path):
    x_values, y_values = [], []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            x_values.append(x)
            y_values.append(y)
    return x_values, y_values

# Read data from the output files
x_values_exact, y_values_exact = read_data('output.txt')
x_values_rk, y_values_rk = read_data('values.txt')

# Find the index of x=0.2 in the lists
index_exact = np.abs(np.array(x_values_exact) - 0.2).argmin()
index_rk = np.abs(np.array(x_values_rk) - 0.2).argmin()

# Plot the data
plt.figure(figsize=(10, 6))

# Plot the exact solution
plt.plot(x_values_exact, y_values_exact, label='Exact Solution', color='blue', linestyle='-', linewidth=2)
plt.scatter(x_values_exact[index_exact], y_values_exact[index_exact], color='blue', marker='o', label='x=0.2 (Exact)')

# Plot the Runge-Kutta solution with scatter plot for better visibility
for i in range(len(x_values_rk)-1):
    color = 'red' if x_values_rk[i] < 0.2 <= x_values_rk[i+1] else 'orange'
    plt.plot(x_values_rk[i:i+2], y_values_rk[i:i+2], color=color, linestyle='-', linewidth=2)
    if x_values_rk[i] < 0.2 <= x_values_rk[i+1]:
        plt.scatter(0.2, y_values_rk[i+1], color='red', marker='o', s=100, label='x=0.2 (RK)')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Exact and Runge-Kutta Solutions')

# Adjust the axis limits for better visibility
plt.xlim(0, 1)
plt.ylim(0, 3)

# Show the plot
plt.grid(True)
plt.legend()
plt.savefig("analysis.png")
