from PIL import Image


def resize(im):
    if (im.size[0] > 10 and im.size[1] > 10):
        for x in range(im.size[0]//2):
            for y in range(im.size[1]//2):
                (r,g,b) = im.getpixel( (x*2,y*2) )
                im.putpixel( (x,y) , (r,g,b) ) 
        resize(im)

pic = Image.open("photo.jpeg")
im = resize(pic)
resize(pic)
im.show()
pic.show()









