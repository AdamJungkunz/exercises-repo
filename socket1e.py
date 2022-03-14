import socket


url = input('Enter - ')
urlParts = url.split('/')
if len(urlParts) >= 4:
    host = urlParts[2]
else:
    host = []
print('host:', host)
print('url:', url)
try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    #print('url:', url)
    cmdstring = 'GET '+ url + ' HTTP/1.0\r\n\r\n'
    print('cmdstring:', cmdstring)
    cmd = cmdstring.encode()
    print('cmd:', cmd)
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print('Invalid url. Enter url with formatting "http://<hostname>/<optional info>"')
