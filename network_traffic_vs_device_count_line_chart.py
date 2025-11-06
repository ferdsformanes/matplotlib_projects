import numpy as np
import matplotlib.pyplot as plt

# Refactored data: number of network devices and corresponding network traffic in Mbps
x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])  # Number of network devices
y = np.array([50, 100, 150, 200, 250, 300, 350, 400, 450, 500])  # Network traffic in Mbps

# Update plot title and axis labels
plt.title("Network Traffic Analysis")
plt.xlabel("Number of Network Devices")
plt.ylabel("Network Traffic (Mbps)")

# Plot the data
plt.plot(x, y)
plt.grid(linestyle='--', linewidth=0.5)
plt.show()
