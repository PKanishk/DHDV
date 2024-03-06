import matplotlib.pyplot as plt

a = ["North", "South", "East", "West"]
b = [250, 180, 300, 200]

plt.bar(a, b, color='blue', edgecolor='red')

plt.xlabel('Zones')
plt.ylabel('Sales')
plt.title('Bar Chart')
plt.show()
