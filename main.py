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
is_decimal = False


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
        self.bttn_decim.clicked.connect(self.decimal)
        self.bttn_undo.clicked.connect(self.undo_number)
        self.bttn_clr_entry.clicked.connect(self.clear_entry)
        self.bttn_invert.clicked.connect(self.invert)

    def button_0_clicked(self):
        global string_display
        global float_display
        global current_op
        self.number(0)

    def button_1_clicked(self):
        global string_display
        global float_display
        global current_op
        self.number(1)

    def button_2_clicked(self):
        global string_display
        global float_display
        global current_op
        self.number(2)

    def button_3_clicked(self):
        global string_display
        global float_display
        global current_op
        self.number(3)

    def button_4_clicked(self):
        global string_display
        global float_display
        global current_op
        self.number(4)

    def button_5_clicked(self):
        global string_display
        global float_display
        global current_op
        self.number(5)

    def button_6_clicked(self):
        global string_display
        global float_display
        global current_op
        self.number(6)

    def button_7_clicked(self):
        global string_display
        global float_display
        global current_op
        self.number(7)

    def button_8_clicked(self):
        global string_display
        global float_display
        global current_op
        self.number(8)

    def button_9_clicked(self):
        global string_display
        global float_display
        global current_op
        self.number(9)

    def decimal(self):
        global string_display
        global float_display
        global current_op
        global is_decimal
        try:
            if current_op == 5:
                string_display = "0"
                current_op = 0
            if not is_decimal:
                string_display += "."
                float_display = float(string_display)
                self.lbl_display.setText(str(string_display))
                is_decimal = True
        except Exception as Arg:
            print(Arg)

    def clear(self):
        global string_display
        global float_display
        global total
        global current_num
        global current_op
        global is_decimal
        string_display = "0"
        float_display = 0.0
        current_num = 0.0
        total = 0.0
        current_op = 0
        self.lbl_display.setText(str(float_display))
        is_decimal = False

    def clear_entry(self):
        global string_display
        global float_display
        global current_op
        global is_decimal
        if current_op == 5:
            self.clear()
            return
        string_display = "0"
        float_display = 0.0
        is_decimal = False
        self.lbl_display.setText(str(float_display))

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

    def invert(self):
        global string_display
        global float_display
        global total
        try:
            string_display = float_display * -1
            float_display = float_display * -1
            if current_op == 5:
                total = total * -1
            self.lbl_display.setText(str(float_display))
        except Exception as Args:
            print(Args)

    def calc(self):
        global current_num
        global total
        global current_op
        global is_decimal
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
            try:
                int(string_display)
            except TypeError:
                is_decimal = True
        except ZeroDivisionError as Arg:
            print(Arg)
            self.lbl_display.setText("Divide by 0 Error:")
            current_op = 5
            return True
        except Exception as Arg:
            print(Arg)
            self.lbl_display.setText("Error!")

    def number(self, number):
        global string_display
        global float_display
        global current_op
        try:
            if current_op == 5:
                string_display = "0"
                current_op = 0
            string_display += str(number)
            float_display = float(string_display)
            self.lbl_display.setText(str(float_display))
        except Exception as Arg:
            print(Arg)
            self.lbl_display.setText("Error!")

    def undo_number(self):
        global string_display
        global float_display
        try:
            string_display = (string_display[:len(string_display) - 1])
            if string_display == "":
                string_display = "0"
            float_display = float(string_display)
            self.lbl_display.setText(str(float_display))
        except Exception as Arg:
            print(Arg)

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
            self.bttn_undo.click()
        if event.key() == Key.Key_Period:
            self.bttn_decim.click()


def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
