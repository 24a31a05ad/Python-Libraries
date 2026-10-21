
import matplotlib.pyplot as plt

# Data
subjects = ["Python", "Java", "C", "SQL", "HTML"]
marks = [85, 90, 75, 80, 95]

# Create a bar chart
plt.bar(subjects, marks)

# Add title and labels
plt.title("Marks in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Display the chart
plt.show()
