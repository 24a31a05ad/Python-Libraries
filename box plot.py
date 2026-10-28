
import matplotlib.pyplot as plt

# Data
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# Create a box plot
plt.boxplot(marks)

# Add title and labels
plt.title("Distribution of Student Marks")
plt.ylabel("Marks")

# Display the plot
plt.show()
