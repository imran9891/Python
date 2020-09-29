import socket

def main():
              host='127.0.0.1'
              port=5000
              s=socket.socket()
              s.connect((host,port))

              message=input("-> ")
              while message!='bye':
                            s.send(message.encode())#sending to server
                            ##Receiving reply from server
                            data=s.recv(1024)#receiving from server
                            print("Reply :" +str(data))
                            message=input("->")
              
              s.close()

main()
