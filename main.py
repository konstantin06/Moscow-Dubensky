import sys

from PyQt5.QtGui import QPainter, QColor

from Ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint, random


class Dis(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        a = random.randint(1, 540)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dis()
    ex.show()
    sys.exit(app.exec())
