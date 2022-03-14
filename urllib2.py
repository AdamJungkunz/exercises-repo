import urllib.request

url = input('Enter - ')

print('url:', url)
count = 0
try:
    fhand = urllib.request.urlopen(url)

    for line in fhand:
        #data = mysock.recv(3000)
        #if len(data) < 1:
        #    break
        curLine = line.decode().strip()
        #print('len(curLine):', len(curLine))
        #chars = data.decode()
        #print('len(chars)', len(chars))
        count = count + len(curLine)
        if count <= 3000:
            print(curLine)


    print('total characters:', count)
except:
    print('Invalid url. Enter url with formatting "http://<hostname>/<optional info>"')
