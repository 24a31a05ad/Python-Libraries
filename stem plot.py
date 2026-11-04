
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5, 6]
y = [10, 25, 15, 30, 20, 40]

# Create a stem plot
plt.stem(x, y)

# Add title and labels
plt.title("Stem Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Add grid
plt.grid(True)

# Display the plot
plt.show()
