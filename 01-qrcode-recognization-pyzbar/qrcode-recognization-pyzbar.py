import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance

# 通过Image对象打开图片
img = Image.open('qrcode.png')
img.show()

# 解析图片，获取所有二维码
barcodes = pyzbar.decode(img)
for barcode in barcodes:
    barcodeData = barcode.data.decode()  # 对每个二维码解析成文本
    print(barcodeData)
