import matplotlib.pyplot as plt

activities = ['Sleeping', 'Studying', 'Entertainment', 'Exercise', 'Others']
time_spent = [8, 6, 4, 2, 4]  # hours per day

plt.pie(time_spent, labels=activities, autopct='%1.1f%%', startangle=140)

plt.title("Daily Time Distribution")

plt.show()
