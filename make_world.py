""" Make a Map in Minecraft"""
__author__ = '@damianmooney'
from mcpi import minecraft as minecraft
from mcpi import block as block


def clearZone( alocx, alocz, blocx, blocz ):
    mc.setBlocks( alocx, 1, alocz, blocx, 128, blocz, block.AIR )
    mc.setBlocks( alocx, -5, alocz, blocx, 0, blocz, block.WATER )


if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    clearZone( -128, -128, 128, 128 )
    print('Cleared')
    f = open('world.txt', 'r')  # open your ascii art text file
    mymap = f.read()
    f.close()

    myrows = mymap.split('\n')

    #print(mymap)
    # --start our top corner of world. adjust to get 0,0 ok on map
    x = 100
    z = 85

    for i in myrows: #for each line in our map
        print(i)
        z -=1
        x = 100
        y = 0
        for j in i:  # go through each position on the current line
            x -=1
            if j != " ":  # if the map is not empty blank minecraft then place a grass block
                position = (x, y, z)
                mc.setBlock(position, block.AIR)
                mc.setBlock(position, block.GRASS)
##            elif j == ".":  # place different type of block
##                position = (x, y, z)
##                mc.setBlock(position, block.AIR )
##                mc.setBlock(position, block.WATER )