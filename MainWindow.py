# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow - PythonCalc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 130, 371, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setObjectName("grid_layout")
        self.bttn_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bttn_1.setMinimumSize(QtCore.QSize(56, 56))
        self.bttn_1.setMaximumSize(QtCore.QSize(56, 56))
        self.bttn_1.setObjectName("bttn_1")
        self.grid_layout.addWidget(self.bttn_1, 0, 0, 1, 1)
        self.bttn_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bttn_4.setMinimumSize(QtCore.QSize(56, 56))
        self.bttn_4.setMaximumSize(QtCore.QSize(56, 56))
        self.bttn_4.setObjectName("bttn_4")
        self.grid_layout.addWidget(self.bttn_4, 1, 0, 1, 1)
        self.bttn_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bttn_7.setMinimumSize(QtCore.QSize(56, 56))
        self.bttn_7.setMaximumSize(QtCore.QSize(56, 56))
        self.bttn_7.setObjectName("bttn_7")
        self.grid_layout.addWidget(self.bttn_7, 2, 0, 1, 1)
        self.bttn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bttn_2.setMinimumSize(QtCore.QSize(56, 56))
        self.bttn_2.setMaximumSize(QtCore.QSize(56, 56))
        self.bttn_2.setObjectName("bttn_2")
        self.grid_layout.addWidget(self.bttn_2, 0, 1, 1, 1)
        self.bttn_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bttn_3.setMinimumSize(QtCore.QSize(56, 56))
        self.bttn_3.setMaximumSize(QtCore.QSize(56, 56))
        self.bttn_3.setObjectName("bttn_3")
        self.grid_layout.addWidget(self.bttn_3, 0, 2, 1, 1)
        self.bttn_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bttn_5.setMinimumSize(QtCore.QSize(56, 56))
        self.bttn_5.setMaximumSize(QtCore.QSize(56, 56))
        self.bttn_5.setObjectName("bttn_5")
        self.grid_layout.addWidget(self.bttn_5, 1, 1, 1, 1)
        self.bttn_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bttn_6.setMinimumSize(QtCore.QSize(56, 56))
        self.bttn_6.setMaximumSize(QtCore.QSize(56, 56))
        self.bttn_6.setObjectName("bttn_6")
        self.grid_layout.addWidget(self.bttn_6, 1, 2, 1, 1)
        self.bttn_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bttn_8.setMinimumSize(QtCore.QSize(56, 56))
        self.bttn_8.setMaximumSize(QtCore.QSize(56, 56))
        self.bttn_8.setObjectName("bttn_8")
        self.grid_layout.addWidget(self.bttn_8, 2, 1, 1, 1)
        self.bttn_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bttn_9.setMinimumSize(QtCore.QSize(56, 56))
        self.bttn_9.setMaximumSize(QtCore.QSize(56, 56))
        self.bttn_9.setObjectName("bttn_9")
        self.grid_layout.addWidget(self.bttn_9, 2, 2, 1, 1)
        self.bttn_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bttn_0.setMinimumSize(QtCore.QSize(56, 56))
        self.bttn_0.setMaximumSize(QtCore.QSize(56, 56))
        self.bttn_0.setObjectName("bttn_0")
        self.grid_layout.addWidget(self.bttn_0, 3, 1, 1, 1)
        self.bttn_equl = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bttn_equl.setMinimumSize(QtCore.QSize(56, 56))
        self.bttn_equl.setMaximumSize(QtCore.QSize(56, 56))
        self.bttn_equl.setObjectName("bttn_equl")
        self.grid_layout.addWidget(self.bttn_equl, 3, 2, 1, 1)
        self.bttn_clr = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bttn_clr.setMinimumSize(QtCore.QSize(56, 56))
        self.bttn_clr.setMaximumSize(QtCore.QSize(56, 56))
        self.bttn_clr.setObjectName("bttn_clr")
        self.grid_layout.addWidget(self.bttn_clr, 3, 0, 1, 1)
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.horizontalGroupBox.setGeometry(QtCore.QRect(20, 70, 371, 61))
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bttn_add = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.bttn_add.setMinimumSize(QtCore.QSize(56, 40))
        self.bttn_add.setMaximumSize(QtCore.QSize(56, 40))
        self.bttn_add.setObjectName("bttn_add")
        self.horizontalLayout.addWidget(self.bttn_add)
        self.bttn_sub = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.bttn_sub.setMinimumSize(QtCore.QSize(56, 40))
        self.bttn_sub.setMaximumSize(QtCore.QSize(56, 40))
        self.bttn_sub.setObjectName("bttn_sub")
        self.horizontalLayout.addWidget(self.bttn_sub)
        self.bttn_divid = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.bttn_divid.setMinimumSize(QtCore.QSize(56, 40))
        self.bttn_divid.setMaximumSize(QtCore.QSize(56, 40))
        self.bttn_divid.setObjectName("bttn_divid")
        self.horizontalLayout.addWidget(self.bttn_divid)
        self.bttn_multi = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.bttn_multi.setMinimumSize(QtCore.QSize(56, 40))
        self.bttn_multi.setMaximumSize(QtCore.QSize(56, 40))
        self.bttn_multi.setObjectName("bttn_multi")
        self.horizontalLayout.addWidget(self.bttn_multi)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 371, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_display = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(16)
        self.lbl_display.setFont(font)
        self.lbl_display.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_display.setObjectName("lbl_display")
        self.horizontalLayout_2.addWidget(self.lbl_display)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bttn_1.setText(_translate("MainWindow", "1"))
        self.bttn_4.setText(_translate("MainWindow", "4"))
        self.bttn_7.setText(_translate("MainWindow", "7"))
        self.bttn_2.setText(_translate("MainWindow", "2"))
        self.bttn_3.setText(_translate("MainWindow", "3"))
        self.bttn_5.setText(_translate("MainWindow", "5"))
        self.bttn_6.setText(_translate("MainWindow", "6"))
        self.bttn_8.setText(_translate("MainWindow", "8"))
        self.bttn_9.setText(_translate("MainWindow", "9"))
        self.bttn_0.setText(_translate("MainWindow", "0"))
        self.bttn_equl.setText(_translate("MainWindow", "="))
        self.bttn_clr.setText(_translate("MainWindow", "Clear"))
        self.bttn_add.setText(_translate("MainWindow", "+"))
        self.bttn_sub.setText(_translate("MainWindow", "-"))
        self.bttn_divid.setText(_translate("MainWindow", "/"))
        self.bttn_multi.setText(_translate("MainWindow", "*"))
        self.lbl_display.setText(_translate("MainWindow", "0"))
