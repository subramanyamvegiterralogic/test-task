import socket

host = socket.gethostname()
port = 586
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send(b'Hello, World')
data = s.recv(1024)
s.close()
print('Received ', repr(data))