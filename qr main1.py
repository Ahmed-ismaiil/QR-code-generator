import qrcode

data=input("Please enter the url or the data you want to encode in QR\n")
qr= qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
#create the Image
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")

#save the image
qrname=input("please enter the name of the file to save\n")
img.save("qrname.png")
print("✅ QR code Generated")