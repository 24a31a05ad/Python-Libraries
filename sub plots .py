
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

# Create two subplots
plt.subplot(1, 2, 1)
plt.plot(x, y1, marker="o")
plt.title("Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.subplot(1, 2, 2)
plt.bar(x, y2)
plt.title("Bar Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()
