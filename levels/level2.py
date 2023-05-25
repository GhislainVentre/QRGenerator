import qrcode

def generate_qr_code():
    qr = qrcode.QRCode(version=20,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4
                )
    qr.add_data('www.google.com')
    qr.make(fit=True)

    img = qr.make_image()
    type(img)
    img.save("your_qr2.png")