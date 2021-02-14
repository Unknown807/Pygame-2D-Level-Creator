# native imports

# external imports

# custom imports

class BaseTile(object):
    def __init__(self,):
        self.image = None
        self.x = None
        self.y = None

    def setX(self, value):
        self.x = value

    def setY(self, value):
        self.y = value

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setImage(self, image):
        self.image = image
    
    def getImage(self):
        return self.image
