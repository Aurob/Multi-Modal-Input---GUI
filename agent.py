import socket
import MySQLdb

class agent_server:
    def __init__(self, ip, port):
        self.HOST = ip
        self.PORT = port
        self.BUFFER_SIZE = 1024
        #self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def start_server(self):
        print("starting agent server...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            connections = []
            while 1:
                conn, addr = s.accept()
                print('Connected by', addr)
                try:
                    data = conn.recv(1024)
                    #if data != '()':
                    print(data.decode())
                    if data.decode() == 'close':
                        break
                    conn.close()
                except:
                    conn.close()
                    break

if __name__ == '__main__':
    try:
        ip = sys.argv[0]
        port = sys.argv[1]

    except:
        ip = input("server ip: ")
        port = input("server port: ")

    server = agent_server(ip,int(port))
    server.start_server()
    

