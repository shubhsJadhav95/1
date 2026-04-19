import socket, threading

c = socket.socket()
c.connect(("localhost", 12345))

threading.Thread(target=lambda: [print(c.recv(1024).decode()) for _ in iter(int,1)], daemon=True).start()

while True:
    c.send(input().encode())