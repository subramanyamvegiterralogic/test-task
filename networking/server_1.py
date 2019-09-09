import socket

# Create Socket Object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local Machine Name
host = socket.gethostname()
port = 9999

# Bind to the port
server_socket.bind((host,port))

# Queue up to 5 requests
server_socket.listen(5)

while True:
    # Establish a connection
    client_socket, addr = server_socket.accept()
    print("Got a connection from %s" % str(addr))

    msg = 'Thank you for connecting'+ "\r\n"
    client_socket.send(msg.encode('ascii'))
    client_socket.close()