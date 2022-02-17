#Source https://towardsdatascience.com/generate-qrcode-with-python-in-5-lines-42eda283f325

import qrcode

input_data = "https://www.youtube.com/"# Link for website

qr = qrcode.QRCode(
        version=1, #Size 1-40
        box_size=10,#Number of pixels
        border=5) #Thickness of border
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')