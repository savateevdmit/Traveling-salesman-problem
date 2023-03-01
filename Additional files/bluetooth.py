import serial as serial

s = serial.Serial("COM4", 9600)

a = [[0, 0], [0, 3], [2, 3], [2, 0]]
a.append([0, 0])
# a.append([0, 0])
for i in range(len(a)):
    if i != 0:
        s.write(bytes(a[i]))