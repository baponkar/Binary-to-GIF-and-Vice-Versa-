import numpy as np
import imageio
from PIL import Image

# Load the binary file into a numpy array
data = np.fromfile("binary_file.bin", dtype=np.uint8)

# Define the dimensions of each frame in the GIF video
width, height = 320, 240

# Calculate the total number of frames in the video
num_frames = len(data) // (width * height)

# Initialize the list of frames for the GIF video
frames = []

# Convert each frame of the binary file into an Image object
for i in range(num_frames):
    frame_data = data[i*width*height:(i+1)*width*height]
    frame = Image.frombytes("L", (width, height), bytes(frame_data))
    frames.append(frame)

# Save the frames as a GIF video using imageio
imageio.mimsave("output.gif", frames, fps=30)
