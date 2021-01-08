# use somebody else's code
from mcpi.minecraft import Minecraft, ChatEvent
from mcpi.minecraftstuff import MinecraftDrawing, MinecraftTurtle

name = "JeremyTsui"
# connect to minecraft
address = "localhost"
mc = Minecraft.create(address)
md = MinecraftDrawing(mc)
turtle = MinecraftTurtle(mc)

# get the x,y,z (position)
entity_id = mc.getPlayerEntityId(name)
# position = mc.entity.getPos(entity_id)

# print position to screen
while True:
    position = mc.entity.getTilePos(entity_id)
    x, y, z = position.x, position.y, position.z
    # mc.postToChat("x: {}, y: {}, z: {}".format(position.x, position.y, position.z))
    # md.drawHollowSphere(x, y, z, 5, 20, 0)
    # turtle.setposition(x, y, z)
    events = mc.events.pollChatPosts()
    for e in events:
        print("{} post a msg: {}".format(mc.entity.getName(e.entityId), e.message))

    for he in mc.events.pollBlockHits():
        print("{} hit a block: {} {}".format(mc.entity.getName(he.entityId), he.pos, he.face))

    for pe in mc.events.pollProjectileHits():
        # print(pe)
        x, y, z = str(pe.pos.x), str(pe.pos.y), str(pe.pos.z)
        if len(pe.targetName) == 0:
            print("{} hit a block({}, {}, {})".format(pe.originName, x, y, z))
        else:
            print("{} hit {}({}, {}, {})".format(pe.originName, pe.targetName, x, y, z))
