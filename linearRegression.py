"""
Created on Sun 14 Apr 18:23:45 2024
Developed by João Gabriel
@rpjoaogabriel on GitHub
https://www.linkedin.com/in/joaogabrielrp/
Created on Sun 14 Apr 18:23:45 2024
Basic Linear Regression using random values for demonstration
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate linear regression data
np.random.seed(0)
# Number of data points
num_points = 100
# Slope and intercept of the line
slope = 2.5
intercept = 7.0

# Generate random x values
x_values = np.random.rand(num_points) * 10

# Generate y values with noise
noise = np.random.normal(0, 2, num_points)
y_values = slope * x_values + intercept + noise

# Perform linear regression
# In this simple example, we know the true values of slope and intercept,
# but in practice, you would use a linear regression algorithm to estimate them.
estimated_slope, estimated_intercept = np.polyfit(x_values, y_values, 1)

# Plot the data points
plt.scatter(x_values, y_values, label='Data points')

# Plot the true linear regression line
plt.plot(x_values, slope * x_values + intercept, color='red', label='True line')

# Plot the estimated linear regression line
plt.plot(x_values, estimated_slope * x_values + estimated_intercept, color='green', label='Estimated line')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression Example')
plt.legend()
plt.grid(True)
plt.show()
