from PIL import Image


im = Image.open("photo.jpeg")

pic = Image.new('RGB',(im.size[0]//2,im.size[1]//2), (0,0,0))

for x in range(im.size[0]//2):
    for y in range(im.size[1]//2):
        (r,g,b) = im.getpixel( (x*2,y*2) )
        pic.putpixel( (x,y) , (r,g,b) ) 

im.show()
pic.show()









