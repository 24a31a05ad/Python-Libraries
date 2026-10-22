
import matplotlib.pyplot as plt

# Data
languages = ["Python", "Java", "C", "JavaScript"]
students = [40, 25, 20, 15]

# Create a pie chart
plt.pie(students, labels=languages, autopct="%1.1f%%")

# Add title
plt.title("Programming Languages Preferred by Students")

# Display the chart
plt.show()
