import sys

from PyQt5.QtGui import QPainter, QColor

from Ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import random


class Dis(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        a = int(random.randint(1, 400))
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(100, 50, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dis()
    ex.show()
    sys.exit(app.exec())
