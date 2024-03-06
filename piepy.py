import matplotlib.pyplot as plt

categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment']
expenses = [30, 25, 20, 25]
colors = ['blue', 'green', 'orange', 'red']

plt.pie(expenses, labels=categories, colors=colors, autopct='%1.1f%%')

plt.title("Household Expenses Distribution")

plt.axis('equal')
plt.show()
