import serial


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
    # print(s.readline())
    data = s.readline().decode()
    # print(data, type(data), len(data))
    # split the microbit data into x, y, z, a, b
    data_s = data.rstrip().split(' ')

    x, y, z = int(data_s[0]), int(data_s[1]), int(data_s[2])
    a = True if data_s[3] == "True" else False
    b = True if data_s[4] == "True" else False
    print((x, y, z, a, b))

while True:
    read_microbit_data()
