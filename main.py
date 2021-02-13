# native imports
import tkinter as tk
from tkinter.constants import X

# external imports

# custom imports
from toolbar import ToolBarFrame
from tileframe import TileFrame

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("1280x600")
        self.title("Pygame Level Creator")
        self.font = ("System", 16, "bold")

        self.TILE_MODE = "Floor"
        
        self.TILESET = None

        self.MAP_WIDTH = 256
        self.MAP_HEIGHT = 256

        self.TILESET_WIDTH = None
        self.TILESET_HEIGHT = None

        # Widget Definitions

        self.toolbar = ToolBarFrame(self, bd=1, relief="raised")
        self.tileframe = TileFrame(self)

        self.bind("<Left>", lambda e: self.toolbar.shiftTiles("LEFT"))
        self.bind("<Right>", lambda e: self.toolbar.shiftTiles("RIGHT"))

        # Widget Placement

        self.toolbar.pack(side="top", fill="x")
        self.tileframe.pack(side="top", fill="both", expand=True)

        self.SELECTED_TILE = self.toolbar.selected_tile

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
    
    def getTileSet(self):
        return self.TILESET
    
    def getSelectedTile(self):
        x = self.SELECTED_TILE.getX()
        y = self.SELECTED_TILE.getY()
        image = self.SELECTED_TILE.getImage()
        return (x, y, image)
    
    def getMapWidth(self):
        return self.MAP_WIDTH
    
    def getMapHeight(self):
        return self.MAP_HEIGHT

    def getTileSetWidth(self):
        return self.TILESET_WIDTH
    
    def getTileSetHeight(self):
        return self.TILESET_HEIGHT

if __name__ == "__main__":
    root = Main()
    root.mainloop()