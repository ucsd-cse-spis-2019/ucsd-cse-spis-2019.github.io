from PIL import Image


def resize(im):
    pic = Image.new('RGB',(im.size[0]//2,im.size[1]//2),(0,0,0))
    for x in range(im.size[0]//2):
        for y in range(im.size[1]//2):
            (r,g,b) = im.getpixel( (x,y) )
            pic.putpixel( (x,y) , (r,g,b) ) 
    return pic

im = Image.open("photo.jpeg")
newpic = resize(im)
im.show()
newpic.show()









