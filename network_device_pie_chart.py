import matplotlib.pyplot as plt

# Simulated API response data
device_automation_data = {
    'Routers': 120,
    'Switches': 200,
    'Firewalls': 80,
    'Access Points': 150,
    'Load Balancers': 50
}

# Pie chart setup
labels = device_automation_data.keys()
sizes = device_automation_data.values()
colors = ['gold', 'lightblue', 'lightcoral', 'yellowgreen', 'violet']
explode = [0.1 if size == max(sizes) else 0 for size in sizes]  # highlight largest slice

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Device Type Percentage')
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
plt.tight_layout()
plt.show()