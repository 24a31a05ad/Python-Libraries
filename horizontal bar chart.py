
import matplotlib.pyplot as plt

# Data
subjects = ["Python", "Java", "SQL", "C", "HTML"]
marks = [85, 90, 80, 75, 95]

# Create a horizontal bar chart
plt.barh(subjects, marks, color="skyblue")

# Add title and labels
plt.title("Student Marks by Subject")
plt.xlabel("Marks")
plt.ylabel("Subjects")

# Display the chart
plt.show()
