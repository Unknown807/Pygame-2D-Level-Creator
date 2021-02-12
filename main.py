# native imports
import tkinter as tk

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
        self.MAP_WIDTH = None
        self.MAP_HEIGHT = None

        # Widget Definitions

        self.toolbar = ToolBarFrame(self, bd=1, relief="raised")

        self.tileframe = TileFrame(self)

        # Widget Placement

        self.toolbar.pack(side="top", fill="x")
        self.tileframe.pack(side="top", fill="both", expand=True)

    def setTileSet(self, value):
        self.TILESET = value
    
    def setMapWidth(self, value):
        self.MAP_WIDTH = value

    def setMapHeight(self, value):
        self.MAP_HEIGHT = value

if __name__ == "__main__":
    root = Main()
    root.mainloop()