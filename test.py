import numpy as np
import matplotlib.pyplot as plt
import h5py


# data path
path_to_depth = './data/nyu_depth_v2_labeled.mat'

# Load the .mat file using h5py
f = h5py.File(path_to_depth)

rgb = f['images']
depth = f['depths']

print(rgb[0].shape)

# Visualize the data
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Plot the RGB image
ax[0].imshow(rgb[0])
ax[0].axis('off')
ax[0].set_title('RGB Image')

# Plot the depth map as a heat map
ax[1].imshow(depth[0], cmap='hot', interpolation='nearest')
ax[1].axis('off')
ax[1].set_title('Depth Map')

plt.show()