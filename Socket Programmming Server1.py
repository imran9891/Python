import socket

s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen(5)##at a time 5 connection can be connected to the server
while True:
              c,addr=s.accept()
              print(c)
              print("got a connection from", addr)
              c.send("Thank you for connecting".encode())
              c.close() #close the connection
