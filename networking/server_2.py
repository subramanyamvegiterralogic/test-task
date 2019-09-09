import socket

host = socket.gethostname()
port = 586

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn, address = s.accept()
print('Connected BY : ',address)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)
conn.close()