# native imports
import tkinter as tk
from tkinter import filedialog

# external imports

# custom imports

class ScrollFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Widget Defintions

        self.scroll_canvas = tk.Canvas(self, bd=0, highlightthickness=0)
        self.frame = tk.Frame(self.scroll_canvas)
        self.scroll_bar_y = tk.Scrollbar(self, orient="vertical", command=self.scroll_canvas.yview)
        self.scroll_bar_x = tk.Scrollbar(self, orient="horizontal", command=self.scroll_canvas.xview)

        self.scroll_canvas.configure(
            yscrollcommand=self.scroll_bar_y.set,
            xscrollcommand=self.scroll_bar_x.set
        )

        # Widget Placement

        self.scroll_bar_y.pack(side="right", fill="y")
        self.scroll_bar_x.pack(side="bottom", fill="x")

        self.scroll_canvas.pack(side="left")
        self.canvas_window = self.scroll_canvas.create_window((0,0), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>", lambda e: self.adjustScrollRegion)

    def adjustScrollRegion(self):
        self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all"))

    def hideHorizontalScrollBar(self):
        self.scroll_bar_x.pack_forget()

    def hideVerticalScrollBar(self):
        self.scroll_bar_y.pack_forget()


class TileSetSelectionDialog(tk.Toplevel):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.geometry("200x300")
        self.title("Select Tileset")
        self.font = ("System", 14, "bold")

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
        self.destroy()
            