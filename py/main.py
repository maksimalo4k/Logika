from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton

def show_win():
    victory = QMessageBox()
    victory.setText("це правильна выдповідь")
    victory.exec_()

def show_lose():
    victory = QMessageBox()
    victory.setText("це не правильна выдповідь")
    victory.exec_()

aplication = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("конкурс від Ситуна Максима")
main_window.resize(1000, 400)

question = QLabel('Скільки класів в школі?')

btn1 = QRadioButton("5")
btn2 = QRadioButton("7")
btn3 = QRadioButton("11")
btn4 = QRadioButton("4")

main_leyoutV = QVBoxLayout()
leyoutH1 = QHBoxLayout()
leyoutH2 = QHBoxLayout()
leyoutH3 = QHBoxLayout()

leyoutH1.addWidget(question, alignment = Qt.AlignCenter)
leyoutH2.addWidget(btn1, alignment = Qt.AlignCenter)
leyoutH2.addWidget(btn2, alignment = Qt.AlignCenter)
leyoutH3.addWidget(btn3, alignment = Qt.AlignCenter)
leyoutH3.addWidget(btn4, alignment = Qt.AlignCenter)

main_leyoutV.addLayout(leyoutH1)
main_leyoutV.addLayout(leyoutH2)
main_leyoutV.addLayout(leyoutH3)

main_window.setLayout(main_leyoutV)

btn3.clicked.connect(show_win)
btn1.clicked.connect(show_lose)
btn2.clicked.connect(show_lose)
btn4.clicked.connect(show_lose)

main_window.show()
aplication.exec_()