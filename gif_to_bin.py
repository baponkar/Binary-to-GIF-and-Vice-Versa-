import numpy as np
from PIL import Image

# Load the GIF video file
frames = Image.open("output.gif")

# Define the dimensions of each frame in the GIF video
width, height = frames.size

# Calculate the total number of frames in the video
num_frames = frames.n_frames

# Initialize the numpy array to store the binary data
data = np.zeros((num_frames, width * height), dtype=np.uint8)

# Extract the binary data from each frame of the GIF video
for i in range(num_frames):
    frames.seek(i)
    frame_data = np.array(frames.convert("L")).flatten()
    data[i] = frame_data

# Save the binary data as a file
data.tofile("binary_file_reverse.bin")
