import xmlrpc.client

# Connect to server
client = xmlrpc.client.ServerProxy("http://127.0.0.1:12345/")

# Call remote functions
print("Addition:", client.add(10, 5))
print("Subtraction:", client.sub(10, 5))