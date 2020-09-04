import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("192.168.137.195",888))

while True:
    a=''
    
    a=input()
    
    s.send(bytes(a,"utf-8"))
    
    if a==  "kapat":
        break

s.close