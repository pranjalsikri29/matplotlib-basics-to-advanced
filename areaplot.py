import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
hours_studied = [2, 3, 4, 3, 5, 6, 1]

plt.plot(days, hours_studied, color='blue')
plt.fill_between(days, hours_studied, color='skyblue', alpha=0.4)

plt.title("Study Hours Over a Week")
plt.xlabel("Day")
plt.ylabel("Hours Studied")

plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
