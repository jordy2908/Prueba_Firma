# Import pyqrcode
import pyqrcode
# URL or string which will represent the QR code
def qr():
    url = "Firmado por: Jordy buestan" # INFORMACION QUE APARECERA AL ESCANERAR QR
    # Generate QR code
    qr_code = pyqrcode.create(url) # GENERACION DE QR

    qr_code.png("image.png", scale=1)