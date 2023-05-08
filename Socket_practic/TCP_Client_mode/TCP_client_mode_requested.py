import socket

port = int(input("Port No: "))
address = ("localhost", port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET,socket,)

while True:
    data = c_socket.recv(BUFSIZE).decode()
    try:
        resp = table[data]
    except:
        c_socket.send("Try aagin".encode())
    else:
        c_socket.send(resp.encode())