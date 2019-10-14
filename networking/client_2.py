import socket

host = socket.gethostname()
port = 586
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
while True:
    msg = input('Enter Message to Send\t:\t')
    msg.encode()
    s.send(msg)
    data = s.recv(1024)
    print('Received ', repr(data))
# s.close()
