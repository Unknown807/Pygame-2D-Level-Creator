# native imports
import tkinter as tk
from tkinter import filedialog

# external imports

# custom imports

class TileSetSelectionDialog(tk.Toplevel):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.geometry("200x300")
        self.title("Select Tileset")
        self.font = ("System", 14, "bold")

        self.parent = parent
        self.controller = controller

        # Widget Defintions

        # For the width of the map (has to be a multiple of 32)
        self.width_label = tk.Label(self, text="Map Width:", font=self.font)
        self.width_entry = tk.Entry(self, font=self.font)

        # For the height of the map (has to be a multiple of 32)
        self.height_label = tk.Label(self, text="Map Height", font=self.font)
        self.height_entry = tk.Entry(self, font=self.font)

        self.tileset_button = tk.Button(self, text="Select Tileset", 
            font=self.font, command=self.selectTileSet)

        self.submit_button = tk.Button(self, text="Submit", 
            font=self.font, command=self.submitTileSet)

        # Widget Placement

        self.width_label.pack(side="top", fill="y", expand=True, padx=5, pady=5)
        self.width_entry.pack(side="top", fill="y", expand=True, padx=5, pady=5)
        self.height_label.pack(side="top", fill="y", expand=True, padx=5, pady=5)
        self.height_entry.pack(side="top", fill="y", expand=True, padx=5, pady=5)
        self.tileset_button.pack(side="top", fill="y", expand=True, padx=5, pady=5)
        self.submit_button.pack(side="top", fill="y", expand=True, padx=5, pady=5)

        self.focus_set()
        self.grab_set()

    def selectTileSet(self):
        filepath = filedialog.askopenfilename(
            initialdir="/",
            title="Select Tileset",
            filetypes = (("png files", "*.png"),),
        )
        filename = filepath.split("/")[-1]
        if filepath != "":
            self.controller.setTileSet(filepath)
            self.tileset_button.configure(text=filename)

    def submitTileSet(self):
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())
        self.controller.setMapWidth(width)
        self.controller.setMapHeight(height)
        self.parent.loadTileSet()
        self.destroy()
        self.grab_release()