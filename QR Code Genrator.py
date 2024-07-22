import qrcode
from PIL import Image
import qrcode.constants

# Prompt user for the URL
url = input("Please enter the URL to generate QR code: ")

# Create a QR Code object with specified parameters
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)

# Add data to the QR Code object
qr.add_data(url)
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill_color='red', back_color='blue')

# Save the QR code image
img.save('chat_gpt_new.png')

print("QR code generated and saved as 'chat_gpt_new.png'")
