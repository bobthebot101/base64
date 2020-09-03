import base64

file = open('output.txt', 'rb')
byte = file.read()

fh = open('output.jpg', 'wb')
fh.write(base64.b64decode((byte)))
fh.close()
