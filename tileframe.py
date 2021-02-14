# native imports
import tkinter as tk

# external imports

# custom imports
from scrollframe import ScrollFrame
from maptile import MapTile
from utils import createTransparentRect

class TileFrame(ScrollFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = parent
        self.scroll_canvas.configure(bg="white")
        
        self.tiles = []

        self.RGB_R = (65535,0,0)
        self.RGB_B = self.RGB_R[::-1]

    def createMap(self):
        self.scroll_canvas.delete("all")
        self.tiles = []

        map_width = self.controller.getMapWidth()
        map_height = self.controller.getMapHeight()

        startx = int(640-(map_width/2))

        for i in range(int(map_width/32)):
            for j in range(int(map_height/32)):
                tile = MapTile()
                drawn_tile = self.scroll_canvas.create_image((startx+i*33,20+j*33), image=tile.getImage(), anchor="nw")
                self.scroll_canvas.tag_bind(drawn_tile, "<Button-1>", self.setTile)
                self.scroll_canvas.tag_bind(drawn_tile, "<Button-3>", self.removeTile)
                tile.setCanvasImageRef(drawn_tile)
                self.tiles.append(tile)
        
        self.adjustScrollRegion()
    
    def setTile(self, event):
        mode = self.controller.getMode()
        event_tile = self.scroll_canvas.find_closest(event.x, event.y)[0]
        if mode == "floor":
            self.setNewTile(event_tile)
        elif mode == "wall":
            self.setWallTile(event_tile)
        else:
            self.setOverlayTile(event_tile)
    
    def removeTile(self, event):
        event_tile = self.scroll_canvas.find_closest(event.x, event.y)[0]
        map_tile = self.findMapTile(event_tile, "floor")
    
        map_tile.reset()
        map_tile.setCanvasImageRef(event_tile) 
        self.scroll_canvas.itemconfigure(event_tile, image=map_tile.getImage())

    def findMapTile(self, canvas_tile, mode):
        for tile in self.tiles:
            if mode == "floor":
                ref_tile = tile.getCanvasImageRef()
            elif mode == "wall":
                ref_tile = tile.getCanvasWallRef()
            else:
                ref_tile = tile.getCanvasOverlayRef()
            if ref_tile == canvas_tile:
                return tile

    def setNewTile(self, canvas_tile):
        x, y, image = self.controller.getSelectedTile()
        if x is None or y is None:
            return

        tile = self.findMapTile(canvas_tile, "floor")
        tile.setImage(image)
        self.scroll_canvas.itemconfigure(tile.getCanvasImageRef(), image=image)
        tile.setX(x)
        tile.setY(y)

    def setWallTile(self, canvas_tile):
        map_tile = self.findMapTile(canvas_tile, "floor")
        x, y = self.scroll_canvas.coords(canvas_tile)

        image = createTransparentRect(self.RGB_R)
        map_tile.setWallImage(image)
        
        drawn_tile = self.scroll_canvas.create_image((x,y), image=image, anchor="nw")
        self.scroll_canvas.tag_bind(drawn_tile, "<Button-1>", self.removeWallTile)
        
        map_tile.setCanvasWallRef(drawn_tile)
        map_tile.setWall(1)
    
    def removeWallTile(self, event):
        wall_tile = self.scroll_canvas.find_closest(event.x, event.y)[0]
        map_tile = self.findMapTile(wall_tile, "wall")

        if map_tile is None: return

        map_tile.setCanvasWallRef(None)
        map_tile.setWallImage(None)
        map_tile.setWall(0)

        self.scroll_canvas.delete(wall_tile)

    def setOverlayTile(self, canvas_tile):
        map_tile = self.findMapTile(canvas_tile, "floor")
        x, y = self.scroll_canvas.coords(canvas_tile)

        image = createTransparentRect(self.RGB_B)
        map_tile.setOverlayImage(image)
        
        drawn_tile = self.scroll_canvas.create_image((x,y), image=image, anchor="nw")
        self.scroll_canvas.tag_bind(drawn_tile, "<Button-1>", self.removeOverlayTile)
        
        map_tile.setCanvasOverlayRef(drawn_tile)
        map_tile.setOverlay(1)
    
    def removeOverlayTile(self, event):
        overlay_tile = self.scroll_canvas.find_closest(event.x, event.y)[0]
        map_tile = self.findMapTile(overlay_tile, "overlay")
        
        if map_tile is None: return

        map_tile.setCanvasOverlayRef(None)
        map_tile.setOverlayImage(None)
        map_tile.setOverlay(0)

        self.scroll_canvas.delete(overlay_tile)

    def toggleWallTiles(self, state):
        for tile in self.tiles:
            self.scroll_canvas.itemconfigure(tile.getCanvasWallRef(), state=state)

    def toggleOverlayTiles(self, state):
        for tile in self.tiles:
            self.scroll_canvas.itemconfigure(tile.getCanvasOverlayRef(), state=state)
        
    
