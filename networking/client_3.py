import socket,sys

host = socket.gethostname()
port = 586
s= None
for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue

    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('Could not open socket')
    sys.exit(1)
s.send(b'Hello , World')
data = s.recv(1024)
s.close()
print('Received ',repr(data))