import matplotlib.pyplot as plt

# Sample dataset
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
sales = [5000, 6000, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 9500, 9000, 10000]

# Plotting
plt.plot(months, sales, marker='o', color='blue')
plt.title('Monthly Sales Performance')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=90)
plt.show()
