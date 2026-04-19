import socket, threading

s = socket.socket()
s.bind(("127.0.0.3", 12345))
s.listen()

clients = []

def handle(c):
    while True:
        try:
            msg = c.recv(1024)
            for client in clients:
                client.send(msg)
        except:
            clients.remove(c)
            c.close()
            break

print("Server started")

while True:
    c, _ = s.accept()
    clients.append(c)
    threading.Thread(target=handle, args=(c,), daemon=True).start()