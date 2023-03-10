import random
import numpy as np
from PIL import Image

image = Image.new('RGB', (2048, 2048))
pixels = image.load()

# Generate random pixel colors for the texture map
for x in range(2048):
  for y in range(2048):
    pixels[x, y] = (252, 204, 132)	
    #pixels[x,y]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
# Save the texture map to a .png file
image.save('texture_face.png', 'PNG')

with open('image02202.mtl', 'w') as f:
  # Write the header for the .mtl file
  f.write('# Generated by Python\n')
  f.write('newmtl FaceTexture\n')
  f.write('map_Kd texture_face.png\n')