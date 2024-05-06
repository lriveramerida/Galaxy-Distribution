import numpy as np

# Load data from GalaxyLocation.txt into a NumPy array
data = np.genfromtxt('GalaxyLocation.txt', dtype=None, delimiter=',', names=True, encoding=None)

# Save to a new text file
np.savetxt('loaded_galaxy_data.txt', data, fmt='%s', delimiter=',', header=','.join(data.dtype.names), comments='')

# Print the loaded data
print("Loaded data saved to loaded_galaxy_data.txt")

