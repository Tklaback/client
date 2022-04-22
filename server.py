import socket

HOST = ''
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            
            message = input()
            if message == '':
                conn.close()
                break
            conn.send(f'{message}'.encode())
            