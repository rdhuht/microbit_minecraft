import serial
from starwarscraft import *
from mcpi.minecraft import Minecraft
import bomb
import time

PORT = "COM9"  # 这里的数字10需要检查一下，去设备管理器里，看看是数字多少，替换即可
BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
# read the first line and flush any bad data
s.readline()


def read_microbit_data():
    # data = s.readline().decode().rstrip().split(' ')
    # x, y, z = int(data[0]), int(data[1]), int(data[2])
    # print(s.readline())
    data = str(s.readline()).rstrip()[2:-5].split(' ')
    # print(type(data))
    # print(data)
    # print(len(data))
    if len(data) > 1:
        x, y, z = int(data[0]), int(data[1]), int(data[2])
        a, b = data[3], data[4]
        a = True if data[3] == "True" else False
        b = True if data[4] == "True" else False
        print(x, y, z, a, b)
        return x, y, z, a, b
    else:
        return 0, 0, 0, False, False


mc = Minecraft.create()
print("连接成功")
# name = input("Your name:")
name = "Jerry"

try:
    pid = mc.getPlayerEntityId(name)
    playerPos = mc.entity.getTilePos(pid)
    print("玩家位置是({}, {}, {})".format(playerPos.x, playerPos.y, playerPos.z))
    craftPos = playerPos.clone()
    craftPos.y -= 3
    craft = XWingFighter(craftPos)
    print("战斗机生成")
    bomb = bomb.Bomb()

    while True:
        time.sleep(0.2)
        x, y, z, a, b = read_microbit_data()
        if a:
            mc.postToChat("A")
            if craft.flying:
                craft.stop()
                mc.postToChat('stop')
            else:
                craft.fly(0.15)
                mc.postToChat('fly')
        if b:
            mc.postToChat('b')
            bpos = craft.craftShape.position
            bomb.drop(bpos.x, bpos.y - 1, bpos.z, 0.1)
            mc.postToChat('bomb!')

        # 调整偏航角度（左右转弯）
        if x > 750:
            print('-->')
            craft.turn(10)
        if x > 500:
            print('->')
            craft.turn(5)
        if x < -750:
            print('<--')
            craft.turn(-10)
        if x < -500:
            craft.turn(-5)
            print('<-')
        if -500 < x < 500:
            craft.turn(0)

        # 拉升/俯冲
        if y > 750:
            print('^^')
            craft.pull(10)
        if y > 500:
            print('^')
            craft.pull(5)
        if y < -750:
            print('dd')
            craft.pull(-10)
        if y < -500:
            craft.pull(-5)
            print('d')
        if -500 < y < 500:
            craft.pull(0)

finally:
    sleep(1)
    craft.clear()
    s.close()
