import socket

# The Public Intwork Interface
host = socket.gethostbyname(socket.gethostname())

# Crete Raw socket and Bind it to public interface
s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((host,0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# Receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# Receive a package
print(s.recvfrom(65565))

# Disable pramiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)