import base64 

with open('IMG_3490.jpg', 'rb') as imagefile:
  byteform = base64.b64encode(imagefile.read())


f = open('output.txt', 'wb')
f.write(byteform)
f.close()
