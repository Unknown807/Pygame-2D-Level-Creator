# native imports
import tkinter as tk

# external imports

# custom imports
from utils import ScrollFrame, TileSetSelectionDialog


class ToolBarFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = parent

        # Widget Defintions

        self.collection_frame = tk.Frame(self)
        self.tileset_button = tk.Button(self.collection_frame, text="Select Tileset",
            font=self.controller.font, command=self.selectTileSet)
        self.export_button = tk.Button(self.collection_frame, text="Export Level", 
            font=self.controller.font, command=self.exportLevel)
        self.mode_label = tk.Label(self.collection_frame, text="MODE: Floor", font=self.controller.font)

        self.tile_ribbon = ScrollFrame(self)
        self.tile_ribbon.scroll_canvas.configure(height=100)
        self.tile_ribbon.hideVerticalScrollBar()

        # Widget Placement

        self.collection_frame.pack(side="left", fill="both")
        self.tileset_button.pack(side="top", fill="y", expand=True, padx=5, pady=5)
        self.export_button.pack(side="top", fill="y", expand=True, padx=5, pady=5)
        self.mode_label.pack(side="top", fill="y", expand=True, padx=5, pady=5)
        self.tile_ribbon.pack(side="right", fill="x", expand=True, padx=5, pady=5)

        for i in range(50):
            tk.Label(self.tile_ribbon.inner_frame, text="LabeL: {}".format(i), font=self.controller.font).pack(side="left", fill="x", expand=True, padx=5, pady=5)
    
    def selectTileSet(self):
        new_tileset = TileSetSelectionDialog(self, self.controller)

    def loadTileSet(self):
        pass

    def exportLevel(self):
        pass