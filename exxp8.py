servers = ["S1", "S2", "S3"]
index = 0

def get_server():
    global index
    server = servers[index]
    index = (index + 1) % len(servers)
    return server

# Simulate requests
for i in range(6):
    print(f"Request {i} -> {get_server()}")