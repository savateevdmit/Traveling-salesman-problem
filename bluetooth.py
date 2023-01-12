import serial as serial

s = serial.Serial("COM4", 9600)
a = [[0, 0], [3, 1], [7, 4], [9, 4], [9, 0], [4, 7], [2, 6], [2, 9]]
a.append([0, 0])
for i in range(len(a)):
    if i != 0:
        s.write(bytes(a[i]))