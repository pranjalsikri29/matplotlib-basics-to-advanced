import matplotlib.pyplot as plt

# Data for both plots
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]
y2 = [5, 15, 20, 22, 28]

# Create a figure with 1 row and 2 columns
plt.subplot(1, 2, 1)  # (rows, columns, plot_number)
plt.plot(x, y1, color='blue')
plt.title("Line Plot")

plt.subplot(1, 2, 2)
plt.bar(x, y2, color='green')
plt.title("Bar Plot")

# Add space between plots
plt.tight_layout()
plt.show()
