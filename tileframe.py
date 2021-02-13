# native imports
import tkinter as tk

# external imports

# custom imports
from utils import (ScrollFrame, MapTile, createTransparentRect)

class TileFrame(ScrollFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = parent
        self.scroll_canvas.configure(bg="white")
        
        self.tiles = []
        self.wall_imgs = []
        self.overlay_imgs = []

        self.RGB_R = (65535,0,0)
        self.RGB_B = self.RGB_R[::-1]

    def createMap(self):
        self.scroll_canvas.delete("all")
        self.tiles = []
        self.wall_imgs = []
        self.overlay_imgs = []

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
        mode = self.controller.getMode()
        event_tile = self.scroll_canvas.find_closest(event.x, event.y)[0]
        if mode == "floor":
            self.setNewTile(event_tile)
        elif mode == "wall":
            self.setWallTile(event_tile)
        else:
            self.setOverlayTile(event_tile)
    
    def findMapTile(self, canvas_tile):
        for tile in self.tiles:
            ref_tile = tile.getCanvasImageRef()
            if ref_tile == canvas_tile:
                return tile

    def findMapTileWithWall(self, wall_tile):
        for tile in self.tiles:
            ref_tile = tile.getCanvasWallRef()
            if ref_tile == wall_tile:
                return tile

    def setNewTile(self, canvas_tile):
        x, y, image = self.controller.getSelectedTile()
        if x is None or y is None:
            return

        tile = self.findMapTile(canvas_tile)
        tile.setImage(image)
        self.scroll_canvas.itemconfigure(tile.getCanvasImageRef(), image=image)
        tile.setX(x)
        tile.setY(y)

    def setWallTile(self, canvas_tile):
        map_tile = self.findMapTile(canvas_tile)
        x, y = self.scroll_canvas.coords(canvas_tile)

        image = createTransparentRect(self.RGB_R)
        self.wall_imgs.append(image)
        
        drawn_tile = self.scroll_canvas.create_image((x,y), image=image, anchor="nw")
        self.scroll_canvas.tag_bind(drawn_tile, "<Button-1>", self.removeWallTile)
        
        map_tile.setCanvasWallRef(drawn_tile)
        map_tile.setWall(1)
    
    def removeWallTile(self, event):
        wall_tile = self.scroll_canvas.find_closest(event.x, event.y)[0]
        map_tile = self.findMapTileWithWall(wall_tile)

        map_tile.clearCanvasWallRef()
        map_tile.setWall(0)

        self.scroll_canvas.delete(wall_tile)

    def setOverlayTile(self, canvas_tile):
        print("Set Overlay Tile")

    def hideWallTiles(self):
        for tile in self.tiles:
            self.scroll_canvas.itemconfigure(tile.getCanvasWallRef(), state="hidden")

    def hideOverlayTiles(self):
        pass

    def showWallTiles(self):
        for tile in self.tiles:
            self.scroll_canvas.itemconfigure(tile.getCanvasWallRef(), state="normal")

    def showOverlayTiles(self):
        pass


        
    
