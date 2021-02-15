# native imports

# external imports
from PIL import ImageTk, Image

# custom imports

def loadImage(imagepath):
    image = Image.open(imagepath)
    return image

def getTileFromImage(x, y, image):
    crop_rect = (x*32, y*32, (x*32)+32, (y*32)+32)
    cropped_img = image.crop(crop_rect)
    return ImageTk.PhotoImage(cropped_img)

def createTransparentRect(fill):
    fill = fill + (int(0.5*255),)
    image = Image.new("RGBA", (32, 32), fill)
    image = ImageTk.PhotoImage(image)
    return image 