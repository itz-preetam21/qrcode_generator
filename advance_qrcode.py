import qrcode 
from PIL import Image,ImageColor,ImageDraw

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

qr.add_data("https://github.com/itz-preetam21")
qr.make(fit=True)

img=qr.make_image(fill_color="red",back_color="blue")

img=img.convert("RGBA")
img.save("preetam_github.png")