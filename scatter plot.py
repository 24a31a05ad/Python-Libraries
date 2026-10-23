
import matplotlib.pyplot as plt

# Data
hours = [1, 2, 3, 4, 5, 6]
marks = [35, 45, 50, 60, 75, 85]

# Create a scatter plot
plt.scatter(hours, marks)

# Add title and labels
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

# Display the plot
plt.show()
