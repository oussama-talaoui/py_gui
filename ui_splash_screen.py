# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash_screen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SplashScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.drop_shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(40, 43, 75, 255));\n"
"color:rgb(100, 194, 202);\n"
"border-radius: 10px;\n"
"}")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.label_title = QtWidgets.QLabel(self.drop_shadow_frame)
        self.label_title.setGeometry(QtCore.QRect(0, 20, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("background-color: none;")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_description = QtWidgets.QLabel(self.drop_shadow_frame)
        self.label_description.setGeometry(QtCore.QRect(0, 50, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("background-color: none;\n"
"color:rgb(150, 150, 150)")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.drop_shadow_frame)
        self.progressBar.setGeometry(QtCore.QRect(30, 130, 321, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"background-color: rgb(120, 120, 124);\n"
"border-style: none;\n"
"color: rgb(220, 220, 220);\n"
"border-radius: 8px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"border-radius: 8px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.488636, stop:0 rgba(52, 153, 216, 255), stop:1 rgba(85, 255, 127, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.drop_shadow_frame)
        self.label_loading.setGeometry(QtCore.QRect(0, 140, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("background-color: none;\n"
"color:rgb(150, 150, 150)")
        self.label_loading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.label_credit = QtWidgets.QLabel(self.drop_shadow_frame)
        self.label_credit.setGeometry(QtCore.QRect(10, 200, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_credit.setFont(font)
        self.label_credit.setStyleSheet("background-color: none;\n"
"color:rgb(150, 150, 150)")
        self.label_credit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_credit.setObjectName("label_credit")
        self.verticalLayout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "System Monitor"))
        self.label_description.setText(_translate("MainWindow", "Zinus Corp."))
        self.label_loading.setText(_translate("MainWindow", "Loading..."))
        self.label_credit.setText(_translate("MainWindow", "By: Oussama Talaoui"))

