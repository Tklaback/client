import socket 
from datetime import datetime
from playsound import playsound



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.1.16', 65432)) #'10.0.0.126'
    running = True
    while running:
        data = s.recv(1024)
        if data: 
            playsound("test.wav")
            now = datetime.now().time()
            print((now, data.decode()))
        else:
            break
