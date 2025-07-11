import matplotlib.pyplot as plt

categories = ['Python', 'Java', 'C++', 'JavaScript', 'SQL']
popularity = [80, 65, 50, 70, 60]

# Create the bar chart
plt.bar(categories, popularity, color='skyblue')

# Add labels and title
plt.title("Programming Language Popularity")
plt.xlabel("Languages")
plt.ylabel("Popularity (%)")

# Show the plot
plt.show()
