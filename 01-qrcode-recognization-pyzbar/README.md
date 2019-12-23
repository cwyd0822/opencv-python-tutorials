# zbar图片二维码识别
通过[zbar](http://zbar.sourceforge.net/)对图片中的二维码进行识别，会将图片中含有的多个二维码图片识别出来。

## 安装python模块
```shell script
pip3 install pyzbar
pip3 install Pillow
```

## 安装系统依赖
mac下通过brew安装zbar
```shell script
brew install zbar
```

## 运行程序
```shell script
python3 qrcode-recognization-pyzbar.py
```