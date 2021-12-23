import serial

PORT = "COM9"
BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

try:
    while True:
        print(s.readline())
        data = str(s.readline()).rstrip()[2:-5].split(' ')
        # data = str(s.readline())
        # print(type(data))
        # print(data)
        # print(len(data))
        if len(data) > 1:
            x, y, z = data[0], data[1], data[2]
            a, b = data[3], data[4]
            print(x, y, z, a, b)


finally:
    s.close()
