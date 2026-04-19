import socket

client = socket.socket()
client.connect(("127.0.0.1", 12345))

while True:
    msg = input("Enter message: ")
    client.send(msg.encode())

    if msg == "exit":
        break

    reply = client.recv(1024).decode()
    print("Server:", reply)

client.close()