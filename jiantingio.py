#!/usr/bin/env python3
import socket,select,time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.0.101',8080))

#s1 = s.recv(64)
#s2 = s.recv(64)

re_list = [s]
#print(re_list)
#read_s, write_s ,err_s = select.select(re_list, [], [])

while True:
    read_s, write_s ,err_s = select.select(re_list, [], [])

    s1=s.recv(64)
    for e in read_s:
        if s1 == b'123':
            c = 1
            print(c)
        if s1== b'456':
            c = 2
            print(c)
            while(1):
                s2 = s.recv(64)
                if s2 == b'run':
                    print("run!!!")
                    c = c + 1
                    print(c)
                    time.sleep(1)
                if s2 == b'stop':
                    print("stop!!!")
                    break
            

