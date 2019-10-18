import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt as Key
import MainWindow as MainWin

float_display: float = 0
string_display: str = "0"
current_num: float = 0
total: float = 0
current_op: int = 0


class MainWindow(QtWidgets.QMainWindow, MainWin.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.bttn_0.clicked.connect(self.button_0_clicked)
        self.bttn_1.clicked.connect(self.button_1_clicked)
        self.bttn_2.clicked.connect(self.button_2_clicked)
        self.bttn_3.clicked.connect(self.button_3_clicked)
        self.bttn_4.clicked.connect(self.button_4_clicked)
        self.bttn_5.clicked.connect(self.button_5_clicked)
        self.bttn_6.clicked.connect(self.button_6_clicked)
        self.bttn_7.clicked.connect(self.button_7_clicked)
        self.bttn_8.clicked.connect(self.button_8_clicked)
        self.bttn_9.clicked.connect(self.button_9_clicked)
        self.bttn_clr.clicked.connect(self.clear)
        self.bttn_add.clicked.connect(self.add)
        self.bttn_sub.clicked.connect(self.subtract)
        self.bttn_equl.clicked.connect(self.equals)
        self.bttn_multi.clicked.connect(self.multiply)
        self.bttn_divid.clicked.connect(self.divide)

    def button_0_clicked(self):
        global string_display
        global float_display
        global current_op
        if current_op == 5:
            string_display = "0"
            current_op = 0
        string_display += "0"
        float_display = float(string_display)
        self.lbl_display.setText(str(float_display))

    def button_1_clicked(self):
        global string_display
        global float_display
        global current_op
        if current_op == 5:
            string_display = "0"
            current_op = 0
        string_display += "1"
        float_display = float(string_display)
        self.lbl_display.setText(str(float_display))

    def button_2_clicked(self):
        global string_display
        global float_display
        global current_op
        if current_op == 5:
            string_display = "0"
            current_op = 0
        string_display += "2"
        float_display = float(string_display)
        self.lbl_display.setText(str(float_display))

    def button_3_clicked(self):
        global string_display
        global float_display
        global current_op
        if current_op == 5:
            string_display = "0"
            current_op = 0
        string_display += "3"
        float_display = float(string_display)
        self.lbl_display.setText(str(float_display))

    def button_4_clicked(self):
        global string_display
        global float_display
        global current_op
        if current_op == 5:
            string_display = "0"
            current_op = 0
        string_display += "4"
        float_display = float(string_display)
        self.lbl_display.setText(str(float_display))

    def button_5_clicked(self):
        global string_display
        global float_display
        global current_op
        if current_op == 5:
            string_display = "0"
            current_op = 0
        string_display += "5"
        float_display = float(string_display)
        self.lbl_display.setText(str(float_display))

    def button_6_clicked(self):
        global string_display
        global float_display
        global current_op
        if current_op == 5:
            string_display = "0"
            current_op = 0
        string_display += "6"
        float_display = float(string_display)
        self.lbl_display.setText(str(float_display))

    def button_7_clicked(self):
        global string_display
        global float_display
        global current_op
        if current_op == 5:
            string_display = "0"
            current_op = 0
        string_display += "7"
        float_display = float(string_display)
        self.lbl_display.setText(str(float_display))

    def button_8_clicked(self):
        global string_display
        global float_display
        global current_op
        if current_op == 5:
            string_display = "0"
            current_op = 0
        string_display += "8"
        float_display = float(string_display)
        self.lbl_display.setText(str(float_display))

    def button_9_clicked(self):
        global string_display
        global float_display
        global current_op
        if current_op == 5:
            string_display = "0"
            current_op = 0
        string_display += "9"
        float_display = float(string_display)
        self.lbl_display.setText(str(float_display))

    def clear(self):
        global string_display
        global float_display
        global total
        global current_num
        global current_op
        string_display = "0"
        float_display = 0.0
        current_num = 0.0
        total = 0.0
        current_op = 0
        self.lbl_display.setText("0.0")

    def add(self):
        global string_display
        global float_display
        global current_op
        if self.calc():
            return
        current_op = 1
        float_display = 0
        string_display = str(float_display)
        self.lbl_display.setText(string_display)

    def subtract(self):
        global string_display
        global float_display
        global current_op
        if self.calc():
            return
        current_op = 2
        float_display = 0
        string_display = str(float_display)
        self.lbl_display.setText(string_display)

    def multiply(self):
        global string_display
        global float_display
        global current_op
        if self.calc():
            return
        current_op = 3
        float_display = 0
        string_display = str(float_display)
        self.lbl_display.setText(string_display)

    def divide(self):
        global string_display
        global float_display
        global current_op
        if self.calc():
            return
        current_op = 4
        float_display = 0
        string_display = str(float_display)
        self.lbl_display.setText(string_display)

    def equals(self):
        global string_display
        global float_display
        global total
        global current_op
        if self.calc():
            return
        current_op = 5
        float_display = total
        string_display = str(float_display)
        self.lbl_display.setText(string_display)

    def calc(self):
        global current_num
        global total
        global current_op
        try:
            current_num = float(self.lbl_display.text())
            if current_op == 1:
                total += current_num
                return False
            elif current_op == 2:
                total -= current_num
                return False
            elif current_op == 3:
                total *= current_num
                return False
            elif current_op == 4:
                total /= current_num
                return False
            elif current_op == 0:
                total = current_num
                return False
            elif current_op == 5:
                return False
            else:
                print("Current Operation Selector Error")
        except ZeroDivisionError as Arg:
            print(Arg)
            self.lbl_display.setText("Divide by 0 Error:")
            current_op = 5
            return True
        except Exception as Arg:
            print(Arg)
            self.lbl_display.setText("Error!")

    def undo_number(self):
        global string_display
        global float_display
        print("Undo")
        print("Str Display: " + string_display)
        print("Float Display: " + str(float_display))
        print("Str Display Length: " + str(len(string_display)))
        string_display = (string_display[:len(string_display)-1])
        print("Str Display: " + string_display)
        float_display = float(string_display)
        print("Float Display: " + str(float_display))
        self.lbl_display.setText(str(float_display))

    def keyPressEvent(self, event):
        if event.key() == Key.Key_0:
            self.button_0_clicked()
        if event.key() == Key.Key_1:
            self.bttn_1.click()
        if event.key() == Key.Key_2:
            self.bttn_2.click()
        if event.key() == Key.Key_3:
            self.bttn_3.click()
        if event.key() == Key.Key_4:
            self.bttn_4.click()
        if event.key() == Key.Key_5:
            self.bttn_5.click()
        if event.key() == Key.Key_6:
            self.bttn_6.click()
        if event.key() == Key.Key_7:
            self.bttn_7.click()
        if event.key() == Key.Key_8:
            self.bttn_8.click()
        if event.key() == Key.Key_9:
            self.bttn_9.click()
        if event.key() == Key.Key_Slash:
            self.bttn_divid.click()
        if event.key() == Key.Key_Asterisk:
            self.bttn_multi.click()
        if event.key() == Key.Key_Minus:
            self.bttn_sub.click()
        if event.key() == Key.Key_Plus:
            self.bttn_add.click()
        if event.key() == Key.Key_Enter:
            self.bttn_equl.click()
        if event.key() == Key.Key_Backspace:
            self.undo_number()


def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
