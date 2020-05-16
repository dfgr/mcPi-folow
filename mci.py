from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

stone = 1
wool = 35
while(1):
    x, y, z = mc.player.getPos()
    mc.setBlock(x+1, y, z, 1)
