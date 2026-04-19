import socket

server = socket.socket()
server.bind(("127.0.0.1", 12345))
server.listen(1)

conn, addr = server.accept()
print("Connected to", addr)

while True:
    data = conn.recv(1024).decode()
    if data == "exit":
        break
    print("Client:", data)
    conn.send("Message received".encode())

conn.close()
server.close()