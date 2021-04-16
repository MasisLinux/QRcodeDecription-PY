import cv2
from pyzbar import pyzbar

img=cv2.imread('myqrcode.png')
barcodes=pyzbar.decode(img)
for barcode in barcodes:
    barcodeData=barcode.data.decode('utf-8')
    print(f'Result: {barcodeData}')
    