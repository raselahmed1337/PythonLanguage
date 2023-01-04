import pyqrcode

qr = pyqrcode.create("www.github.com/mahmudraselvlog")
qr.png("mygit.png",scale=8)