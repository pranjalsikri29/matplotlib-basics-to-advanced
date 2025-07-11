import matplotlib.pyplot as plt

# Sample data: number of tasks completed each day
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
tasks = [1, 3, 2, 4, 3, 5, 2]

# Convert days to numerical values for plotting
x = range(len(days))

# Create stem plot
plt.stem(x, tasks, linefmt='g-', markerfmt='ro', basefmt='k-')

# Add labels and title
plt.xticks(x, days)  # replace numeric x with day labels
plt.title("Tasks Completed Over the Week")
plt.xlabel("Day")
plt.ylabel("Tasks Done")

# Show plot
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
