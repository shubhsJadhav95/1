from xmlrpc.server import SimpleXMLRPCServer

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# Create server
server = SimpleXMLRPCServer(("127.0.0.1", 12345))
print("Server running on port 12345...")

# Register functions
server.register_function(add, "add")
server.register_function(sub, "sub")

# Start server
server.serve_forever()