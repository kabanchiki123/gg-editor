from PyQt6.QtWidgets import *
from conwerter import pil2pixmap
from PIL import Image
import os

app = QApplication([])
window = QWidget()

mainline = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()

papka_btn = QPushButton("Папка")
vlivo_btn = QPushButton("Вліво")
vpravo_btn = QPushButton("Вправо")
dzerkalo_btn = QPushButton("Дзеркало")
rizkizt_btn = QPushButton("Різкість")
black_add_white = QPushButton("Ч/Б")

photo_list = QListWidget()
photo_lbl = QLabel("фото")

mainline.addLayout(v1)

v1.addWidget(papka_btn)
v1.addWidget(photo_list)

mainline.addLayout(v2)

v2.addWidget(photo_lbl)
v2.addLayout(h1)

h1.addWidget(vlivo_btn)
h1.addWidget(vpravo_btn)
h1.addWidget(dzerkalo_btn)
h1.addWidget(rizkizt_btn)
h1.addWidget(black_add_white)

app.setStyleSheet("""
      QWidget{
            background: #435749;
            }
            
      QPushButton {
            background-color: #0d0e24;
            border-style: ridge ; 
            font-family: Roboto ;
              
"""
)

class ImageProcessor:
    def __init__(self):
        self.folder = ""
        self.filename = ""
        self.image = ""
    def load(self):
        img_path = os.path.join(self.folder, self.filename)
        self.image = Image.open(img_path)

    def show(self):
        pix = pil2pixmap(self.image)
        pix = pix.scaledToWidth(500)
        photo_lbl.setPixmap(pix)


    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.show()

    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.show()

    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.show()

ip = ImageProcessor()
ip.filename = "j.jpeg"
ip.load()
ip.show()


def openfolder(self):
    ip.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(ip.folder)
    photo_list.clear()
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png"):
            photo_list.addItem(file)


def show_chosen_image(self):
    ip.filename = photo_list.currentItem().text()
    ip.load()
    ip.show()



vpravo_btn.clicked.connect(ip.rotate_right)
vlivo_btn.clicked.connect(ip.rotate_left)
photo_list.currentRowChanged.connect(show_chosen_image)
papka_btn.clicked.connect(openfolder)
window.setLayout(mainline)
window.show()
app.exec()
