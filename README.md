# Pygame-2D-Level-Creator

Python version 3.7.3
## Modules Used

* tkinter
* pickle
* pillow - version 8.1.0

## Description

I made this program to help me create 2D levels using tilesets for games in pygame, The output is a '.LEVEL' file which has information on the size of the level, the size of the tilset being used and a list of 4-element tuples containing info about what type of tiles they are.

(0,1,0,0) - the first two elements are the x and y location of the tile. Since each tile in the tileset to be used will always be 32x32, you can get the specified tile by mutilpying x * 32 and y * 32 to get the top left corner of the 32x32 tile you want from the tileset, then pygame would crop it out. the third element is whether the tile is a wall and would block the player in the game from going through it. The fourth element is if the tile is an overlay, whether it should be drawn later over other things because otherwise sprites drawn after might go over them.

## How to Use

![alt text](/imgs/img1.JPG)

When you run the program you will be greeted with an empty window. To create a new level press 'Create Level'. You will then get the popup in the middle. 
* Enter filename you want your level to have at the top in 'Level Name'
* For map width and height you are expected to enter any multiple of 32 (minimum is 128x128 or 64x64 recommended), this doesn't have to be square (e.g 640x480). This means for a level of 256 width and 256 height, the amount of tiles will be 256/32 = 8x8 = 64 total
* The 'Select Tileset button will open up a file explorer, pick the png image of the tileset you want. The tileset has to be a multiple of 32 and square (e.g 512x512).
* The 'Select Ground' button can be ignored for now
* Once done press 'Submit'

![alt text](/imgs/img2.JPG)

Once you have a level set up and a tileset loaded at the top, you can start placing tiles.
* The 'Current Tile' on the top right shows what tile you currently have selected
* To place tiles, select one and left click anywhere, to delete it you can either place a new tile on it or right click and it will go back to the default gray tile
* To cycle through all the tiles at the top you can use the left and right arrow keys

![alt text](/imgs/img3.JPG)

By pressing the numbers: 1, 2, 3, 4 you can switch between different tile creating modes. The 'MODE: <>' label in the top left tells you your current mode
* 1 is the default mode which you lets you place tiles from the toolbar
* 2 is the wall mode, which (as shown above) lets you place walls to indicate which blocks should act as obstacles to the player and prevent them from going through them. You place walls by left clicking and to remove them just left click again

![alt text](/imgs/img4.JPG)

* 3 is the overlay mode, which is similar to wall mode in placing and removing the tiles. The point of adding overlays is so that when a pygame program is reading the level data it can see which blocks are marked as overlays and will collect them and draw them later, so that other sprites 'go under them' when walking through them. For example a player walking through a forest of trees.

![alt text](/imgs/img5.JPG)

Remember the 'Select Ground' button? It allows you to choose another level file (one you created without selecting a ground level) and make it act as the floor underneath this map (in a pygame program, it would draw the ground first, then the level itself). This is so that tiles which don't take up all of the 32x32 space they have will still have a floor underneath them (e.g stone paths in a town).

In the above image I'm creating a level file which I will use as the ground for another level file. Since thats the case I didn't select a ground for this level. You have to make sure to fill in all the tile spaces with a tile (otherwise it won't work when trying to use it as a ground for another level).
* Also make sure when you use a ground level to have both the ground level and the tileset it uses in the same directory as the program

![alt text](/imgs/img6.JPG)

Here I created a new level and then selected the ground file I just made, then by pressing **4** the ground is shown on top of the level in order to help you visualise maybe where certain markings in the ground are and let you place your level tiles correctly. Then to go back to editing the level press **1** for floor mode

To **finish** your level press the 'Export Level' button and it will create a '.LEVEL' file in the same directory as the program
