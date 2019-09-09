import socket

# Create Socket Object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get Local Machine Name
host = socket.gethostname()
port = 9999

# Connection to the hostname on the port
s.connect((host,port))

# Receive Not more than 1024 bytes
msg = s.recv(1024)

s.close()
print(msg.decode('ascii'))