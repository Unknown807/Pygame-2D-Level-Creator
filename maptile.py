# native imports

# external imports

# custom imports
from basetile import BaseTile
from utils import createTransparentRect

class MapTile(BaseTile):
    def __init__(self):

        self.canvas_image_ref = None
        self.canvas_wall_ref = None
        self.canvas_overlay_ref = None
        
        self.setImage(createTransparentRect((0,0,0)))
        self.wall_img = None
        self.overlay_img = None

        self.wall = 0
        self.overlay = 0

    def reset(self):
        self.__init__()
        self.x = None
        self.y = None
    
    # For Wall
    def setWall(self, value):
        self.wall = value
    
    def setCanvasWallRef(self, ref):
        self.canvas_wall_ref = ref

    def setWallImage(self, image):
        self.wall_img = image
    
    def getCanvasWallRef(self):
        return self.canvas_wall_ref

    def getWall(self):
        return self.wall

    def getWallImage(self):
        return self.wall_img

    # For Overlay
    def setOverlay(self, value):
        self.overlay = value
    
    def setCanvasOverlayRef(self, ref):
        self.canvas_overlay_ref = ref

    def setOverlayImage(self, image):
        self.overlay_img = image

    def getOverlay(self):
        return self.overlay
    
    def getOverlayImage(self):
        return self.overlay_img
    
    def getCanvasOverlayRef(self):
        return self.canvas_overlay_ref

    # Other
    def setCanvasImageRef(self, ref):
        self.canvas_image_ref = ref
    
    def getCanvasImageRef(self):
        return self.canvas_image_ref

