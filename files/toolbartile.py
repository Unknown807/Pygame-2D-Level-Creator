# native imports
import tkinter as tk

# external imports

# custom imports
from basetile import BaseTile

class ToolbarTile(tk.Label, BaseTile):
    def __init__(self, parent):
        tk.Label.__init__(self, parent,)
        BaseTile.__init__(self,)

    def setImage(self, image):
        super().setImage(image)
        self.configure(image=self.image)