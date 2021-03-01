import sys
import sqlite3
from Эспрессо_pyy import Ui_MainWindow
from Капучино_addEditCoffeeForm import Ui_MainWindow_2
from PyQt5 import QtWidgets


def main():
    class MyWidget_2(QtWidgets.QMainWindow, Ui_MainWindow_2):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.comboBox.setVisible(False)
            self.textEdit.setVisible(False)
            self.textEdit_2.setVisible(False)
            self.pushButton_5.setVisible(False)
            self.pushButton_4.setVisible(False)
            self.pushButton_5.setText("СОЗДАТЬ")
            self.pushButton_3.clicked.connect(self.exit)
            self.pushButton_2.clicked.connect(self.add)
            self.pushButton.clicked.connect(self.edit)
            self.textEdit.setText("""## верный формат - 
            'ID название сорта степень обжарки молотый/в зернах описание вкуса цена объем упаковки' 
            (удалите это)##""")

        def edit(self):
            self.textEdit_2.setText("Для началы выберете что хотите изменить")
            self.comboBox.setVisible(True)
            self.textEdit_2.setVisible(True)
            self.pushButton_4.setVisible(True)
            self.pushButton_4.clicked.connect(self.edit_2)
            con = sqlite3.connect("Капучино_coffee.db")
            cur = con.cursor()
            result = cur.execute("""SELECT name FROM coffee""").fetchall()
            con.close()
            self.comboBox.activated[str].connect(self.choosen)
            for i in result:
                self.comboBox.addItem(str(i).lstrip("('").rstrip("',)"))

        def edit_2(self):
            try:
                choose = str(self.comboBox.currentText())
                data = self.textEdit_2.toPlainText().split()
                con = sqlite3.connect("Капучино_coffee.db")
                cur = con.cursor()
                cur.execute(f"""UPDATE coffee 
                SET id = '{data[0]}', name = '{data[1]}', power = '{data[2]}', quality = '{data[3]}', taste = '{data[4]}', price = '{data[5]}', capacity = {data[6]}
                WHERE name = '{choose}'""")
                con.commit()
            except sqlite3.Error as e:
                self.textEdit_2.setText("error")
                print(e)
            self.comboBox.setVisible(False)
            self.textEdit_2.setVisible(False)
            self.pushButton_4.setVisible(False)

        def choosen(self, text):
            con = sqlite3.connect("Капучино_coffee.db")
            cur = con.cursor()
            result = str(cur.execute(f"""SELECT * FROM coffee
            WHERE name = '{text}'""").fetchall())
            con.close()
            self.textEdit_2.setText(f"""Текущее значение(удалите пояснение и измените в желаемом объеме):
            {result.lstrip("[(").rstrip(")]")}
            В формате:
            'ID название сорта степень обжарки молотый/в зернах описание вкуса цена объем упаковки'""")
            return

        def add(self):
            self.textEdit.setVisible(True)
            self.pushButton_5.setVisible(True)
            self.pushButton_5.clicked.connect(self.add_2)

        def add_2(self):
            try:
                data = self.textEdit.toPlainText().split()
                con = sqlite3.connect("Капучино_coffee.db")
                cur = con.cursor()
                cur.execute(f"INSERT INTO coffee VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', {data[6]})")
                con.commit()
                self.textEdit.setVisible(False)
                self.pushButton_5.setVisible(False)
            except sqlite3.Error as e:
                self.textEdit.setText("error")
                print(e)

        def exit(self):
            self.w = MyWidget()
            self.w.show()
            self.close()

    class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.pushButton.clicked.connect(self.cofi)
            self.conf = 0

        def cofi(self):
            self.conf += 1
            if self.conf == 2:
                self.w = MyWidget_2()
                self.w.show()
                self.close()
            con = sqlite3.connect("Капучино_coffee.db")
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

