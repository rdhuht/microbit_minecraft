from mcpi.minecraft import Minecraft, ChatEvent
from mcpi.minecraftstuff import MinecraftDrawing, MinecraftTurtle
from mcpi import block, entity

name = "JeremyTsui"
# connect to minecraft
address = "localhost"
mc = Minecraft.create(address)
md = MinecraftDrawing(mc)
turtle = MinecraftTurtle(mc)

# get the x,y,z (position)
entity_id = mc.getPlayerEntityId(name)
position = mc.entity.getPos(entity_id)
x, y, z = int(position.x), int(position.y), int(position.z)

ada = MinecraftTurtle(mc)
ada.setposition(x, y, z)
