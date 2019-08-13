from PIL import Image

img_file = Image.open("chennai_2007.png")
img = img_file.load()

xs, ys = img_file.size

green = 0

for x in range(0, xs):
    for y in range(0, ys):
      _, g, _ = img[x, y]
      green += g

green_avg = green / (xs * ys)
print(green_avg)

green_dev = 0
for x in range(0, xs):
    for y in range(0, ys):
      _, g, _ = img[x, y]
      green_dev += abs(green_avg - g)

green_dev = green_dev / (xs * ys)

print(green_dev)

## GREEN Density

#YEAR GREEN_AVG GREEN_DEVIATION
#Chennai
#2004 105.71333672675695 24.441343162174444
#2007 117.8565887704368 24.698630206246218
#2017 102.39776072169352 22.423569590520923
#Amsterdam
#2004 97.65479635645437 29.838709063109228
#2016 111.31577617892874 26.559536142868133
#Absolute
#gre  135.0 0.0
