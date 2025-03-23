from PyQt6.QtWidgets import *

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

window.setLayout(mainline)
window.show()
app.exec()
