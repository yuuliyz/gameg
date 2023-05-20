from pygame import *
init()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

game = True




app = QApplication([])
scene = QWidget()
scene.resize(900, 700)

button1 = QPushButton('начать игру')
button2 = QPushButton('настройки')
button3 = QPushButton('ааааа')

main_line = QVBoxLayout()
main_line.addWidget(button1, alignment= Qt.AlignCenter)
main_line.addWidget(button2, alignment= Qt.AlignCenter)
main_line.addWidget(button3, alignment= Qt.AlignCenter)

def game():
    if button1.clicked.connect() == True:
        while game:
            



scene.setLayout(main_line)

scene.show
app.exec_
