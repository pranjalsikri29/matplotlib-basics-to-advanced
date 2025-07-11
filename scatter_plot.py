import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 55, 65, 70, 75, 90]

plt.scatter(study_hours, marks, color='green', marker='o')

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid(True)

plt.show()

#True → enable the grid
#False → disable the grid (default)
#plt.grid(True) is a Matplotlib function that adds grid lines to your plot to make it easier to read the data.

