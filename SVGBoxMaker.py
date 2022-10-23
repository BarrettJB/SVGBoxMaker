import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def InitWindow():
    app = QApplication(sys.argv)
    window = QWidget()
    b = QLabel(window)
    b.setText('Hello World!')
    window.setGeometry(100,100,200,50)
    b.move(50,20)
    window.setWindowTitle("PyQt5")
    window.show()
    sys.exit(app.exec_())

class window(QWidget):
    def __init__(self, parent = None):
        super(window, self,).__init__(parent)
        self.resize(200,50)
        self.setWindowTitle("Hi")
        self.label = QLabel(self)
        self.label.setText('Hello World!')
        font = QFont()
        font.setFamily('Arial')
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50,20)

if __name__ == '__main__':
    InitWindow()