from PIL import Image

def flipHorizRect(pic, x, y, width, height):
    ''' horizontally flip the rectangle of size width, height,
        whose top left corner is (x, y), in pic. '''
    for xloc in range(x, x+width):
        xtarget = xloc+width
        for yloc in range(y, y+height):
            ytarget = yloc+height
            source = pic.getpixel((xloc, yloc))
            target = pic.getpixel((xtarget, ytarget))
            pic.putpixel((xtarget, ytarget), source)
            pic.putpixel((xloc, yloc), target)
            ytarget -= 1
        xtarget -= 1

def copyRect(sourcePic, targetPic, x, y, width, height):
    for xloc in range(x, x+width):
        for yloc in range(y, y+height):
            if x >= 0 and y >= 0 and x+width < sourcePic.size()[0] and \
               y+height < targetPic.size()[1]:
                source = sourcePic.getpixel((xloc, yloc))
                targetPic.putpixel((xloc, yloc), source)
                
