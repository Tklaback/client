import socket 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.1.27', 65432))
    running = True
    while running:
        data = s.recv(1024)
        if data:    
            print(data.decode())
        else:
            break
