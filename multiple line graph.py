
import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May"]

python_marks = [70, 75, 80, 85, 90]
java_marks = [60, 65, 70, 75, 80]
sql_marks = [50, 60, 65, 70, 75]

# Plot multiple lines
plt.plot(months, python_marks, marker="o", label="Python")
plt.plot(months, java_marks, marker="s", label="Java")
plt.plot(months, sql_marks, marker="^", label="SQL")

# Add title and labels
plt.title("Subject Marks Comparison")
plt.xlabel("Months")
plt.ylabel("Marks")

# Add legend and grid
plt.legend()
plt.grid(True)

# Display graph
plt.show()
