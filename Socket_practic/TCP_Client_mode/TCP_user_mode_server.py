#My TCP_user_modul_server.py
class TCPServer:
    def __init__(self,port):
        import socket
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind(("localhost",port))
        self.sock.listen(1)

    def Accept(self):
        self.c_sock,self.c_addr = self.sock.accept()
        return self.c_sock, self.c_addr
    
if __name__ == '__main__':
    sock = TCPServer(2500)
    c,addr = sock.Accept()
    print("수신 메세지", c.recv(1024).decode())
    msg = "Hello Client"
    c.send(msg.encode())
    c.clsoe()
