# native imports
import tkinter as tk

# external imports

# custom imports
from utils import ScrollFrame


class ToolBarFrame(ScrollFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
