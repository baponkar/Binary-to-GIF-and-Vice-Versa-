# Binary-to-GIF-and-Vice-Versa 

## You can convert a large binary file into a gif file then it can be uploaded into the YouTube.

Test code from [here](https://colab.research.google.com/drive/1BGZx19csk_feDeu-2PDaKJfst_1iKI2W#scrollTo=K6RnHC73VfOm&line=1&uniqifier=1)
1. Binary to gif 


```
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
```

2. GIF to binary file 

```

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
```
