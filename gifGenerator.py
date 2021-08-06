import os

os.chdir("C:/Users/luisf/Desktop/curvedLine")
# put filenames into an array
files = os.listdir()

import imageio
images = []
for file in files:
    images.append(imageio.imread(file))
imageio.mimsave('../curveMovie.gif', images, duration = 0.25)
