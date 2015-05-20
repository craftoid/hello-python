import PIL
import PIL.Image as Im

# load picture
pic = Im.open("image.png")
pixels = pic.load()

# get image dimensions
xsize, ysize = pic.size

# iterate over all the pixels
# and invert the color value
for x in range(xsize):
	for y in range(ysize):
		r, g, b = pixels[x, y]
		r = 255 - r
		g = 255 - g
		b = 255 - b
		pixels[x, y] = r, g, b

# save to disk
pic.save("new-image.png")

