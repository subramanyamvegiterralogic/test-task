import socket,sys

# host = socket.gethostname()
host = None
port = 586
s= None
for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0 , socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue

    try:
        s.bind(sa)
        s.listen(1)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print('Could not opened socket')
    sys.exit(1)
conn,addr = s.accept()
print('Connected By ', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)
conn.close()