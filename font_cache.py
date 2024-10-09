import matplotlib.pyplot as plt

# Create a simple plot to force `matplotlib` to build the font cache.
plt.plot([0, 1], [0, 1])
plt.title("Test Plot")
plt.show()
