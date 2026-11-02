
import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 180, 220]

# Create an area chart
plt.fill_between(months, sales, color="skyblue", alpha=0.5)

# Add line on the area chart
plt.plot(months, sales, marker="o", color="blue")

# Add title and labels
plt.title("Monthly Sales Growth")
plt.xlabel("Months")
plt.ylabel("Sales")

# Display grid
plt.grid(True)

# Show the chart
plt.show()
