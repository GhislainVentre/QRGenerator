import qrcode


def generate_qr_code():
    img = qrcode.make('www.google.com')
    type(img)  # qrcode.image.pil.PilImage
    img.save("your_qr_code.png")
