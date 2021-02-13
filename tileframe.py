# native imports
import tkinter as tk

# external imports

# custom imports
from utils import (ScrollFrame, MapTile)

class TileFrame(ScrollFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = parent
        self.tiles = []

    def createMap(self):
        self.scroll_canvas.delete("all")

        map_width = self.controller.getMapWidth()
        map_height = self.controller.getMapHeight()

        startx = int(640-(map_width/2))

        for i in range(int(map_width/32)):
            for j in range(int(map_height/32)):
                tile = MapTile()
                drawn_tile = self.scroll_canvas.create_image((startx+i*33,20+j*33), image=tile.getImage(), anchor="nw")
                self.scroll_canvas.tag_bind(drawn_tile, "<Button-1>", self.setTile)
                tile.setCanvasImageRef(drawn_tile)
                self.tiles.append(tile)
        
        self.adjustScrollRegion()
    
    def setTile(self, event):
        x, y, image = self.controller.getSelectedTile()
        if x is None or y is None:
            return
        
        event_tile = self.scroll_canvas.find_closest(event.x, event.y)[0]

        for tile in self.tiles:
            ref_tile = tile.getCanvasImageRef()
            if ref_tile == event_tile:
                tile.setImage(image)
                self.scroll_canvas.itemconfigure(ref_tile, image=image)
                tile.setX(x)
                tile.setY(y)
                break
                

        
    
