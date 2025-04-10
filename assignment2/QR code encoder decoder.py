import qrcode

data= 'don\'t forget to subscribe'
qr =qrcode.QRCode(version=2,box_size=16,border=9)
qr.add_data(data)
qr.make(fit=True)

img =qr.make_image(fill_color='pink', back_color='black')


img.save("C:/Users/TechXcess/Desktop/New folder (11)/ASSIGNMENT 4/myqrcodee.png")


from pyzbar.pyzbar import decode
from PIL import Image


img=Image.open("C:/Users/TechXcess/Desktop/New folder (11)/ASSIGNMENT 4/myqrcodee.png")
result=decode(img)
print(result)