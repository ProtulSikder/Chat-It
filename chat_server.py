import socket

port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("",port))

s.listen(1)
conn, addr = s.accept()

while 1:
    data = conn.recv(1024).decode()

    print(data)

    message = input("-->")

    if message == 'q':
        break
    else:
        conn.send(message.encode())

s.close()
