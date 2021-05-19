from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QAction, QApplication, QLabel, QLineEdit, QMainWindow, QMenu, QPushButton, QVBoxLayout, QWidget

#class LabelPersonalizado(QLabel):


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Practica Eventos')
        self.setFixedSize(QSize(400,300))
        self.label = QLabel("Click en esta ventana")
        self.setCentralWidget(self.label)
        self.setMouseTracking(True)

    # def mouseMoveEvent(self, e):
    #     self.label.setText("mouse en movimiento")
    # 
    # def mousePressEvent(self, e):
    #     self.label.setText("mouse presionado")
    # 
    # def mouseDoubleClickEvent(self, e):
    #     self.label.setText("doble click")


    #Qt.NoButton	0 ( 000)	No se presionó ningún botón o el evento no está relacionado con la presión del botón.
    #Qt.LeftButton	1 ( 001)	Se presiona el botón izquierdo
    #Qt.RightButton	2 ( 010)	Se presiona el botón derecho.
    #Qt.MiddleButton	4 ( 100)	Se presiona el botón central.
    
    def mouseReleaseEvent(self, e):
        if(e.button() == Qt.LeftButton):
            print('click boton izquierdo')
        elif(e.button() == Qt.RightButton):
            print('click boton derecho')
        elif(e.button() == Qt.MiddleButton):
            print('click boton medio')
    
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("opcion 1", self))
        context.addAction(QAction("opcion 2", self))
        context.addAction(QAction("opcion 3", self))
        context.exec(e.globalPos())

        
app = QApplication([])

ventana = MainWindow()
ventana.show()

app.exec_()