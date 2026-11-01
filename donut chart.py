
import matplotlib.pyplot as plt

# Data
languages = ["Python", "Java", "C", "SQL"]
students = [40, 30, 20, 10]

# Create a donut chart
plt.pie(
    students,
    labels=languages,
    autopct="%1.1f%%",
    wedgeprops=dict(width=0.4)
)

# Add title
plt.title("Programming Language Preferences")

# Display the chart
plt.show()
