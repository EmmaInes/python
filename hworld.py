import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for macOS
import matplotlib.pyplot as plt
import numpy as np

# Basic matplotlib examples
print("\nCreating some basic plots...")

# Example 1: Simple line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
plt.title('Simple Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# Example 2: Scatter plot
np.random.seed(42)
x_scatter = np.random.randn(50)
y_scatter = np.random.randn(50)
plt.figure(figsize=(8, 6))
plt.scatter(x_scatter, y_scatter, alpha=0.6, c='red', s=50)
plt.title('Random Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)
plt.show()

# Example 3: Bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue', edgecolor='navy')
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()