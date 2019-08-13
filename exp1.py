from PIL import Image

img_file = Image.open("ams_2016.png")
img = img_file.load()

xs, ys = img_file.size

green = 0

for x in range(0, xs):
    for y in range(0, ys):
      _, g, _ = img[x, y]
      green += g

green_density = green/ (xs * ys)
print(green, green_density)

#YEAR GREEN_VAL GREEN_DENSITY
#Chennai
#2004 110902593 105.71333672675695
#2017 107424262 102.39776072169352
#Amsterdam
#2004 102448475 97.65479635645437
#2016 116780045 111.31577617892874
#Absolute
#gre  1646023680 135.0