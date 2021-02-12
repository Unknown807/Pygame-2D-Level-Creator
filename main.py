# native imports
import tkinter as tk

# external imports

# custom imports
from toolbar import ToolBarFrame
from tileframe import TileFrame
from utils import TileCache

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("1280x600")
        self.title("Pygame Level Creator")
        self.font = ("System", 16, "bold")

        self.TILE_MODE = "Floor"
        
        self.TILESET = None
        self.TILE_CACHE = None

        self.MAP_WIDTH = None
        self.MAP_HEIGHT = None

        self.TILESET_WIDTH = None
        self.TILESET_HEIGHT = None
        # Widget Definitions

        self.toolbar = ToolBarFrame(self, bd=1, relief="raised")
        self.tileframe = TileFrame(self)

        self.bind("<Left>", lambda e: self.toolbar.shiftTilesLeft())
        self.bind("<Right>", lambda e: self.toolbar.shiftTilesRight())

        # Widget Placement

        self.toolbar.pack(side="top", fill="x")
        self.tileframe.pack(side="top", fill="both", expand=True)

    def setTileSet(self, value):
        self.TILESET = value
    
    def setMapWidth(self, value):
        self.MAP_WIDTH = value

    def setMapHeight(self, value):
        self.MAP_HEIGHT = value
    
    def setTileSetWidth(self, value):
        self.TILESET_WIDTH = value
    
    def setTileSetHeight(self, value):
        self.TILESET_HEIGHT = value
    
    def setTileCache(self, width, height):
        self.TILE_CACHE = TileCache(width, height)
    
    def getTileSet(self):
        return self.TILESET
    
    def getMapWidth(self):
        return self.MAP_WIDTH
    
    def getMapHeight(self):
        return self.MAP_HEIGHT

    def getTileSetWidth(self):
        return self.TILESET_WIDTH
    
    def getTileSetHeight(self):
        return self.TILESET_HEIGHT

    def getTileCache(self):
        return self.TILE_CACHE

if __name__ == "__main__":
    root = Main()
    root.mainloop()