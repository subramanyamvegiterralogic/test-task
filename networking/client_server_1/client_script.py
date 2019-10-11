import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if len(sys.argv) != 3:
#     print("Correct usage: script, IP address, port number")
#     exit()
# ip_address = str(sys.argv[1])
# port_number = int(sys.argv[2])
ip_address = socket.gethostname()
port_number = 9999
server.connect((ip_address,port_number))
while True:
    socket_list = [server]
    """ There are two possible input situations. Either the user wants to give  manual input to send to other people, 
        or the server is sending a message  to be printed on the screen. Select returns from sockets_list, the stream that 
        is reader for input. So for example, if the server wants to send a message, then the if condition will hold true 
        below.If the user wants to send a message, the else condition will evaluate as true"""
    # print(socket_list)
    read_socket, write_socket, error_socket = select.select(socket_list,[],[])

    for socks in read_socket:
        if socks == server:
            message = socks.recv(2048)
            print(message)
        else:
            message = sys.stdin.readline()
            server.sendmsg(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
        server.close()
