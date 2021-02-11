# native imports
import tkinter as tk

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