import serial
import time
from spotiget import getSongs
from spotiget import isPlaying
songs = getSongs()
serialPort = "COM5"
s = serial.Serial(serialPort)
s.baudrate = 115200
length = len(songs)
counter = 1
realsongs = []
for i in range(length):
    test = str(counter) + ". " + songs[i]
    realsongs.append(test)
    counter += 1
counter = 0
while True:
    numberator = s.read(1)
    time.sleep(1)
    if numberator is b'4':
        print("B PRESS")
        print(realsongs[counter])
        s.write(bytes(realsongs[counter], 'utf-8'))
        counter += 1
        s.write(b"$")
    elif numberator is b'2':
        print("A PRESS")
        playing = isPlaying()
        if(playing):
            print("Song is playing.")
        else:
            print("Song is NOT playing.")

    numberator = 0
    if counter is 10:
        counter = 0