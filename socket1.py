import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'data.pr4e.org'
print('host:', host)
mysock.connect(('data.pr4e.org', 80))
cmdstring = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'
print('cmdstring:', cmdstring)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
