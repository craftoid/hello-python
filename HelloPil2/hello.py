import PIL
import PIL.Image as Im

# load picture
pic = Im.open("image.png")
pixels = pic.load()

# get image dimensions
xsize, ysize = pic.size

def luminance(color):
	r, g, b = color[:3]
	return int( 0.21 * r + 0.72 * g + 0.07 * b )

# find out the limit, by looking for the mean brightness
limit = 0
for x in range(xsize):
	for y in range(ysize):
		brightness = luminance(pixels[x, y])
		limit += brightness
limit /= (xsize * ysize)

print("Limit: %s." % limit)

# iterate over all the pixels
# and invert the color value
for x in range(xsize):
	for y in range(ysize):
		brightness = luminance(pixels[x, y])
		if brightness > limit:
			brightness = 255
		else:
			brightness = 0
		pixels[x, y] = (brightness,) * 3

# save to disk
pic.save("new-image.png")

