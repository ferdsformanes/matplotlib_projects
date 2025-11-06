import matplotlib.pyplot as plt
import numpy as np

# Network device types
x = np.array(["Router", "Switch", "Firewall", "Access Point"])

# Example bandwidth usage in Mbps
y = np.array([120, 300, 80, 150])

plt.bar(x, y, width=0.4, color='skyblue')
plt.title("Device Type Count")
plt.xlabel("Device Type")
plt.ylabel("Device Count")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()