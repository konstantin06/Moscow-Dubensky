import sys
import sqlite3
from Эспрессо_pyy import Ui_MainWindow
from PyQt5 import QtWidgets


def main():
    class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.pushButton.clicked.connect(self.cofi)

        def cofi(self):
            con = sqlite3.connect("Эспрессо_coffee.db")
            cur = con.cursor()
            result = cur.execute("""SELECT * FROM coffee""").fetchall()
            con.close()
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setRowCount(len(result))
            for i in range(len(result)):
                for j in range(len(result[i])):
                    self.tableWidget.setItem(int(i), int(j), QtWidgets.QTableWidgetItem(result[i][j]))

    if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        ex = MyWidget()
        ex.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()