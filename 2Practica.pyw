from random import choice
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class MainWindow(QMainWindow):
    def __init__(self):
        #super(MainWindow, self).__init__()
        super().__init__()

        self.n_veces_click = 0

        self.setWindowTitle('Practica2')
        self.setFixedSize(QSize(400,300))

        self.boton_es_verificado = False
        self.boton = QPushButton('PEGAME!!!')
        self.boton.setCheckable(True)
        self.boton.clicked.connect(self.fue_clickeado)

        self.windowTitleChanged.connect(self.the_window)

        self.setCentralWidget(self.boton)

    def fue_clickeado(self, checked):
        print('clickeado')
        nuevo_titulo = choice(window_titles)
        print("cambiando titulo a {}".format(nuevo_titulo))
        self.setWindowTitle(nuevo_titulo)

    def the_window(self, window_title):
        print("titulo cambio a: {}".format(window_title))

        if window_title == "Something went wrong":
            self.button.setDisabled(True)

app = QApplication([])

ventana = MainWindow()
ventana.show()

app.exec_()
