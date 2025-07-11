import matplotlib.pyplot as plt

marks = [45, 55, 67, 70, 72, 75, 78, 80, 82, 85, 86, 88, 90, 91, 93, 95, 97]

plt.hist(marks, bins=7, color='purple', edgecolor='black')

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")


plt.grid(axis='y', linestyle='--', alpha=0.6)
#alpha is used to show tranperancy and opacity 


plt.show()
