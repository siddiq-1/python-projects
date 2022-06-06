from asyncio import QueueEmpty
import imp
from textwrap import fill
from turtle import back, fillcolor
import qrcode
from PIL import Image
import imp
qr=qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=10,border=4,)
qr.add_data("https://youtu.be/lNi3W4aT2_g")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="red")
img.save("qrgenerator1.png")