from PIL import Image, ImageDraw
from datetime import datetime

file_name = "ams_2016"
img_file = Image.open(file_name+'.png')
img = img_file.load()

new_img = Image.new("RGB", img_file.size, "#ffffff")
dctx = ImageDraw.Draw(new_img)

xs, ys = img_file.size

green = 0

for x in range(0, xs):
    for y in range(0, ys):
        r, g, b = img[x, y]
        if r >= 34 and r <= 100 and g >= 60 and g <= 139 and b >= 34 and b <= 100:
            dctx.point([x, y],fill=(0, g, 0))

new_img.save('test_exp5/'+file_name+'_white.png')

#YEAR GREEN_VAL GREEN_DENSITY
#Chennai
#2004 110902593 105.71333672675695
#2017 107424262 102.39776072169352
#Amsterdam
#2004 102448475 97.65479635645437
#2016 116780045 111.31577617892874
#Absolute
#gre  1646023680 135.0