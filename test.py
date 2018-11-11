# import serial
# import struct
# import time
#
#
# arduino = serial.Serial(port="COM6", baudrate=9600)
# to_send = "10101".encode('ascii')#struct.pack('>5B', 1, 0, 1, 0, 1)
# print("Sending ", to_send)
# # print(arduino.read())
# while True:
# #     print("Recieving ", arduino.readline())
#     time.sleep(0.5)
#     arduino.write([1, 0, 1])
#     print("Here")
#     time.sleep(2)
#
# arduino.close()

test = '0000000'
print([int(i) for i in test])