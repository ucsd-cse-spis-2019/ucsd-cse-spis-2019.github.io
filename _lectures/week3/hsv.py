# Convert to HSV color space

from PIL import Image
import colorsys    

# Convert an image from RGB to HSV
# It returns a new image 
def RGB2HSV(img_source):
    img_target = Image.new('RGB',(pic.size[0],pic.size[1]),(0,0,0))
    for x in range(img_source.size[0]):
        for y in range(img_source.size[1]):
            (r,g,b) = img_source.getpixel((x,y))
            h,s,v = colorsys.rgb_to_hsv(r/255.,g/255.,b/255.)
            img_target.putpixel((x,y), (int(h*255.0),int(s*255.0),int(v*255.0)))
    return img_target


# Convert an image from HSV to RGB
# It returns a new image
def HSV2RGB(img_source):
    img_target = Image.new('RGB',(pic.size[0],pic.size[1]),(0,0,0))
    for x in range(img_source.size[0]):
        for y in range(img_source.size[1]):
            (h,s,v) = img_source.getpixel((x,y))
            r,g,b = colorsys.hsv_to_rgb(h/255.,s/255.,v/255.)
            img_target.putpixel((x,y), (int(r*255.0),int(g*255.0),int(b*255.0)))
    return img_target

# Filter an HSV image. It modifies the image itself (nothing is returned)
def filterHSV(img):
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            (h,s,v) = img.getpixel((x,y))
            if (h > 30) and (h < 50) and (v > 200) and (s > 100):
                # keep color
                img.putpixel((x,y), (h,s,v))
            else:
                # set to black
                img.putpixel((x,y), (0,0,0))


# Open file
pic = Image.open('originals/homerprof.jpg')
pic.show()

# Convert to HSV
pic_hsv = RGB2HSV(pic)
pic_hsv.show()

# Filter HSV image
filterHSV(pic_hsv)

# Convert to RGB
pic_rgb = HSV2RGB(pic_hsv)
pic_rgb.show()



