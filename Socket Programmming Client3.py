import socket

def main():
              host='127.0.0.1'
              port=5000
              s=socket.socket()
              s.connect((host,port))

              message=input("-> ")
              while message!='q':
                            s.send(message.encode())
                            data=s.recv(1024)
                            print("received from server :",data())
                            message=input("->")
              s.close()

main()
