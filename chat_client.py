import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = input("Enter the server IP address:") #IP address of your server(use ifconfig/ipconfig to find it)
port = 5555

s.connect((host,port))

message = input("-->")

while message != 'q':
    s.send(message.encode())

    data = s.recv(1024).decode()

    print(data)

    message = input("-->")

s.close()
