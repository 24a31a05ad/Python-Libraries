
import matplotlib.pyplot as plt

# Data
years = [2021, 2022, 2023, 2024, 2025]
students = [50, 65, 80, 95, 120]

# Create a line graph
plt.plot(years, students, marker="o", color="blue")

# Add title and labels
plt.title("Student Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Students")

# Add grid
plt.grid(True)

# Save the graph as an image
plt.savefig("student_growth.png")

# Display the graph
plt.show()
