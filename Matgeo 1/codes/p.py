import matplotlib.pyplot as plt
import numpy as np

# Load the angle from the text file
with open("angle.txt", "r") as f:
    angle_degrees = float(f.read().strip())

# Convert the angle to radians
angle_radians = np.radians(angle_degrees)

# Vector components (original)
v_rain = -30.0  # Vertical speed of rain
v_woman = 10.0  # Woman's speed

# Calculate original vector components
x_original = v_woman * np.cos(angle_radians)
y_original = v_rain + v_woman * np.sin(angle_radians)

# Calculate vector components in opposite direction (negate both x and y)
x_opposite = -x_original
y_opposite = -y_original

# Plot the vectors
plt.figure(figsize=(5, 5))

# Plot original vector (blue)
plt.quiver([0], [0], [x_original], [y_original], angles='xy', scale_units='xy', scale=1, color='blue', label='Original Direction')

# Plot opposite vector (red) with label
plt.quiver([0], [0], [x_opposite], [y_opposite], angles='xy', scale_units='xy', scale=1, color='red', label='Direction of Umbrella')

plt.xlim(-40, 40)
plt.ylim(-40, 40)
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Vertical distance (m)")
plt.title("Vector representing the direction of the umbrella (and its opposite)")
plt.grid(True)
plt.legend()  # Add legend to differentiate vectors
plt.show()
