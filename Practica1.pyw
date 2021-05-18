from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PRACTICA 1")
        self.setFixedSize(QSize(400,300))

        button = QPushButton('presioname')
        button.clicked.connect(self.a)
        self.setCentralWidget(button)
    
    def a(self):
        print('pulso!')

app = QApplication([])

ventana = MainWindow()
ventana.show()

app.exec_()