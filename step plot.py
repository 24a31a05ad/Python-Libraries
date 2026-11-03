
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6]
sales = [10, 20, 15, 30, 25, 40]

# Create a step plot
plt.step(days, sales, where="mid", marker="o")

# Add title and labels
plt.title("Daily Sales Report")
plt.xlabel("Days")
plt.ylabel("Sales")

# Add grid
plt.grid(True)

# Display the plot
plt.show()
