# native imports
import tkinter as tk

# external imports
from PIL import ImageTk

# custom imports
from utils import (
    ScrollFrame, TileSetSelectionDialog, 
    loadImage, getTileFromImage, ToolbarTile
)


class ToolBarFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = parent
        self.TILE_X = 0
        self.TILE_Y = 0

        self.ROW_LEN = None

        # Widget Defintions

        self.collection_frame = tk.Frame(self)
        self.tileset_button = tk.Button(self.collection_frame, text="Select Tileset",
            font=self.controller.font, command=self.selectTileSet)
        self.export_button = tk.Button(self.collection_frame, text="Export Level", 
            font=self.controller.font, command=self.exportLevel)
        self.mode_label = tk.Label(self.collection_frame, text="MODE: floor", font=self.controller.font)

        self.tile_ribbon = ScrollFrame(self)
        self.tile_ribbon.scroll_canvas.configure(height=100)
        self.tile_ribbon.hideVerticalScrollBar()

        self.selected_tile_frame = tk.Frame(self)

        self.selected_tile_label = tk.Label(self.selected_tile_frame, text="Current Tile:", font=self.controller.font)
        self.selected_tile = ToolbarTile(self.selected_tile_frame)
        self.selected_tile.setImage(ImageTk.PhotoImage(loadImage("defaulttile.png")))

        # Widget Placement

        self.collection_frame.pack(side="left", fill="both")
        self.tileset_button.pack(side="top", fill="y", expand=True, padx=5, pady=5)
        self.export_button.pack(side="top", fill="y", expand=True, padx=5, pady=5)
        self.mode_label.pack(side="top", fill="y", expand=True, padx=5, pady=5)
        self.selected_tile_frame.pack(side="right", padx=5, pady=5)
        self.selected_tile_label.pack(side="top", fill="y", expand=True, padx=2, pady=2)
        self.selected_tile.pack(side="top", fill="y", expand=True, padx=2, pady=2)
        self.tile_ribbon.pack(side="right", fill="x", expand=True, padx=5, pady=5)

        for i in range(2):
            for j in range(32):
                tile = ToolbarTile(self.tile_ribbon.inner_frame)
                tile.grid(row=i, column=j)
                tile.bind("<Button-1>", self.selectTile)

    def selectTile(self, event):
        tile = event.widget
        self.selected_tile.setImage(tile.getImage())
        self.selected_tile.setX(tile.getX())
        self.selected_tile.setY(tile.getY())

    def selectTileSet(self):
        #new_tileset = TileSetSelectionDialog(self, self.controller)
        self.controller.setTileSet("C:\\Users\\Teks Viler\\Documents\\PYGAMESTUFF\\test1\\tileset2.png")
        self.loadTileSet()
        self.controller.tileframe.createMap()

    def loadTileSet(self):
        self.TILE_X = 0
        self.TILE_Y = 0
        self.ROW_LEN = None

        for tile in self.tile_ribbon.inner_frame.winfo_children():
            tile.clearImage()

        loaded_tileset = loadImage(self.controller.getTileSet())
        self.controller.setTileSet(loaded_tileset)

        tileset_width, tileset_height = loaded_tileset.size
        self.controller.setTileSetWidth(tileset_width)
        self.controller.setTileSetHeight(tileset_height)

        self.loadNewTiles()

    def loadNewTiles(self):
        tileset = self.controller.getTileSet()
        tileset_width = self.controller.getTileSetWidth()

        limit = int(tileset_width/32)

        for tile in self.tile_ribbon.inner_frame.winfo_children():
            if (self.TILE_Y > limit-1):
                break

            image = getTileFromImage(self.TILE_X, self.TILE_Y, tileset)
            tile.setImage(image)
            tile.setX(self.TILE_X)
            tile.setY(self.TILE_Y)

            self.TILE_X += 1
            if self.TILE_X == limit:
                self.TILE_Y += 1
                self.TILE_X = 0

    def shiftTiles(self, key):
        tileset_height = self.controller.getTileSetHeight()
        if tileset_height is None: 
            return

        limit = ((tileset_height/32)**2)/64
        if limit <= 1:
            return 

        if self.ROW_LEN is None:
            self.ROW_LEN = self.TILE_Y

        if key == "LEFT":
            if self.TILE_Y <= self.ROW_LEN: return
            self.TILE_Y -= (self.ROW_LEN*2)
        else:
            if self.TILE_Y >= int(tileset_height/32)-1: return

        self.TILE_X = 0
        self.loadNewTiles()

    def exportLevel(self):
        pass