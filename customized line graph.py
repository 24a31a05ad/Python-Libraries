
import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 180, 220]

# Create a customized line graph
plt.plot(
    months,
    sales,
    color="green",
    marker="o",
    linestyle="--",
    linewidth=2,
    markersize=8,
    label="Monthly Sales"
)

# Add title and labels
plt.title("Monthly Sales Report")
plt.xlabel("Months")
plt.ylabel("Sales")

# Display legend and grid
plt.legend()
plt.grid(True)

# Display the graph
plt.show()
