import serial

from starwarscraft import *
# from bomb import Bomb
from mcpi.minecraft import Minecraft

PORT = "COM10"  # 这里的数字10需要检查一下，去设备管理器里，看看是数字多少，替换即可
BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
# read the first line and flush any bad data
s.readline()


def read_microbit_data():
    # read a line from the microbit,
    data = s.readline().decode()
    # print(data)
    # split the microbit data into x, y, z, a, b
    data_s = data.rstrip().split(' ')

    x, y, z = int(data_s[0]), int(data_s[1]), int(data_s[2])
    a = True if data_s[3] == "True" else False
    b = True if data_s[4] == "True" else False
    # debug
    # print(x, y, z, a, b)
    return x, y, z, a, b


mc = Minecraft.create()
print("连接成功")
# name = input("Your name:")
name = "JeremyTsui"

try:
    pid = mc.getPlayerEntityId(name)
    playerPos = mc.entity.getTilePos(pid)
    print("玩家位置是({}, {}, {})".format(playerPos.x, playerPos.y, playerPos.z))
    craftPos = playerPos.clone()
    craftPos.y -= 3
    craft = XWingFighter(craftPos)
    print("战斗机生成")
    # bomb = Bomb()

    while True:
        x, y, z, a, b = read_microbit_data()
        print(x, y, z, a, b)
        if a:
            print("A")
            if craft.flying:
                craft.stop()
                print('stop')
            else:
                craft.fly(0.15)
                print('fly')
        if b:
            print('b')
            bpos = craft.craftShape.position
            # bomb.drop(bpos.x, bpos.y - 1, bpos.z, 0.1)
            XWingFighter.dropTNT()
            print('bomb!')

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

        # 
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
