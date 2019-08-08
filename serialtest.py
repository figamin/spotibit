import serial
import os
from spotiget import getSongs
songs = getSongs()
serialPort = "COM4"
baud = 115200
s = serial.Serial(serialPort)
s.baudrate = baud
length = len(songs)
counter = 1
for i in range(length):
    test = str(counter) + ". " + songs[i]
    #test = songs[i]
    print(test)
    #s.write(bytes(counter))
    #s.write(bytes(". ", 'utf-8'))
    s.write(bytes(test, 'utf-8'))
    counter += 1
    #s.write(b"abcdefghijklmnopqrs;;tuvwxyz1234567890")
s.write(b"$")
s.close()
