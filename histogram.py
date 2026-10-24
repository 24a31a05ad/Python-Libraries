
import matplotlib.pyplot as plt

# Data
marks = [45, 50, 55, 60, 65, 65, 70, 75, 80, 85, 90, 95]

# Create a histogram
plt.hist(marks, bins=5, edgecolor="black")

# Add title and labels
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

# Display the histogram
plt.show()
