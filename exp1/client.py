import socket

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(("127.0.0.1", 12345))

while True:
    # Send message
    msg = input("Client: ")
    client.send(msg.encode())

    if msg == "exit":
        break

    # Receive reply
    reply = client.recv(1024).decode()
    print("Server:", reply)

# Close connection
client.close()