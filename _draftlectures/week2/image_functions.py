from PIL import Image



def resize(im):
    pic = Image.new('RGB',(im.size[0]//2,im.size[1]//2),(0,0,0))
    for x in range(im.size[0]//2):
        for y in range(im.size[1]//2):
            (r,g,b) = im.getpixel( (x*2,y*2) )
            pic.putpixel( (x,y) , (r,g,b) ) 
    return pic


def insert(im1,im2):
    for x in range(im2.size[0]):
        for y in range(im2.size[1]):
            (r,g,b) = im2.getpixel( (x,y) )
            im1.putpixel( (x,y), (r,g,b))


            
pic = Image.open("photo.jpeg")
pic2 = resize(pic)
pic2.show()

insert(pic,pic2)
pic.show()






