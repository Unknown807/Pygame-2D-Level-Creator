# native imports
import tkinter as tk
from tkinter import filedialog

# external imports

# custom imports

class TileSetSelectionDialog(tk.Toplevel):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.geometry("250x350")
        self.title("Select Tileset")
        self.font = ("System", 14, "bold")

        self.parent = parent
        self.controller = controller

        # Widget Defintions

        self.name_label = tk.Label(self, text="Level Name:", font=self.font)
        self.name_entry = tk.Entry(self, font=self.font)

        # For the width of the map (has to be a multiple of 32)
        self.width_label = tk.Label(self, text="Map Width:", font=self.font)
        self.width_entry = tk.Entry(self, font=self.font)

        # For the height of the map (has to be a multiple of 32)
        self.height_label = tk.Label(self, text="Map Height", font=self.font)
        self.height_entry = tk.Entry(self, font=self.font)

        self.tileset_button = tk.Button(self, text="Select Tileset", 
            font=self.font, command=self.selectTileSet)
        
        self.ground_button = tk.Button(self, text="Select Ground",
            font=self.font, command=lambda: self.selectTileSet(True))

        self.submit_button = tk.Button(self, text="Submit", 
            font=self.font, command=self.submitTileSet)

        # Widget Placement

        widgets = (
            self.name_label, self.name_entry, self.width_label, self.width_entry,
            self.height_label, self.height_entry, self.tileset_button, self.ground_button,
            self.submit_button
        )

        for widget in widgets:
            widget.pack(side="top", fill="y", expand=True, padx=5, pady=5)

        self.focus_set()
        self.grab_set()

    def selectTileSet(self, ground=False):
        filepath = filedialog.askopenfilename(
            initialdir="/",
            title="Select Tileset",
            filetypes = (("all files", "*.*"), ("png files", "*.png")),
        )
        filename = filepath.split("/")[-1]
        if filepath != "":
            if ground:
                self.controller.setGround(filename)
                self.ground_button.configure(text=filename)
            else:
                self.controller.setTileSet(filepath)
                self.controller.setTileSetName(filename)
                self.tileset_button.configure(text=filename)

    def submitTileSet(self):
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())
        levelname = self.name_entry.get()

        self.controller.setMapWidth(width)
        self.controller.setMapHeight(height)
        self.controller.setLevelName(levelname)
        
        self.parent.loadTileSet()
        self.controller.createMap()
        self.controller.drawGround()
        self.destroy()
        self.grab_release()