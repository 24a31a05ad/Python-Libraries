
import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 200, 250]

# Create a line graph
plt.plot(months, sales, marker="o", color="blue")

# Add title and labels
plt.title("Monthly Sales Report")
plt.xlabel("Months")
plt.ylabel("Sales")

# Add text to the graph
plt.text("Mar", 130, "Sales Increased")

# Add annotation
plt.annotate(
    "Highest Sales",
    xy=("May", 250),
    xytext=("Mar", 220),
    arrowprops=dict(arrowstyle="->")
)

# Display the graph
plt.show()
