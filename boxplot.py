import matplotlib.pyplot as plt

math_marks = [55, 60, 65, 68, 70, 72, 75, 78, 80, 82, 85, 86, 88, 90, 92]

plt.boxplot(math_marks)

plt.title("Distribution of Math Marks")
plt.ylabel("Marks")

plt.show()
