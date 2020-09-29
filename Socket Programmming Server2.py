import socket

def main():
              host='127.0.0.1'
              port=5000
              s=socket.socket()
              s.bind((host,port))
              s.listen(1)
              c,addr=s.accept()
              print("Connection from:" +str(addr))
              while True:
                            data=c.recv(1024)#receiving from client
                            if not data:
                                          break
                            print("Msg: " +str(data))
                            reply=input("->")
                            c.send(reply.encode())
              c.close()
                            
                            

main()
