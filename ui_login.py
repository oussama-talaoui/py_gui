# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 477)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/system_monitor.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMinimumSize(QtCore.QSize(0, 25))
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.top_bar.setStyleSheet("background-color: rgb(26, 26, 46);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.top_bar)
        self.frame_error.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_error.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_error.setStyleSheet("background-color: rgb(233, 69, 96);\n"
"border-radius: 3px;")
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(15, 0, 5, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.btn_close_popup = QtWidgets.QPushButton(self.frame_error)
        self.btn_close_popup.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_close_popup.setStyleSheet("QPushButton {\n"
"border-radius: 3px;\n"
"font: 75 10pt \"Ubuntu\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 26, 46);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(15, 52, 96);\n"
"}")
        self.btn_close_popup.setObjectName("btn_close_popup")
        self.horizontalLayout_3.addWidget(self.btn_close_popup)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.top_bar)
        self.frame_content = QtWidgets.QFrame(self.centralwidget)
        self.frame_content.setStyleSheet("background-color: rgb(26, 26, 46);")
        self.frame_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_login = QtWidgets.QFrame(self.frame_content)
        self.frame_login.setMinimumSize(QtCore.QSize(250, 400))
        self.frame_login.setMaximumSize(QtCore.QSize(250, 400))
        self.frame_login.setStyleSheet("background-color: rgb(22, 33, 62);")
        self.frame_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login.setObjectName("frame_login")
        self.frame = QtWidgets.QFrame(self.frame_login)
        self.frame.setGeometry(QtCore.QRect(50, 40, 150, 150))
        self.frame.setStyleSheet("border-image: url(:/system_monitor/system_monitor.png);\n"
"background-size: 10 px;\n"
"backgroud-position: center no-repeat;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_user = QtWidgets.QLineEdit(self.frame_login)
        self.lineEdit_user.setGeometry(QtCore.QRect(30, 200, 191, 45))
        self.lineEdit_user.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(26, 26, 46);\n"
"    border-radius: 3px;\n"
"    padding: 15px;\n"
"    background-color: rgb(26, 26, 46);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(100, 100, 100);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_user.setInputMask("")
        self.lineEdit_user.setText("")
        self.lineEdit_user.setMaxLength(32)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame_login)
        self.lineEdit_password.setGeometry(QtCore.QRect(30, 250, 191, 45))
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(26, 26, 46);\n"
"    border-radius: 3px;\n"
"    padding: 15px;\n"
"    background-color: rgb(26, 26, 46);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(100, 100, 100);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setMaxLength(16)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_title = QtWidgets.QLabel(self.frame_login)
        self.label_title.setGeometry(QtCore.QRect(40, 9, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.checkBox_user = QtWidgets.QCheckBox(self.frame_login)
        self.checkBox_user.setGeometry(QtCore.QRect(30, 302, 191, 22))
        self.checkBox_user.setStyleSheet("QCheckBox::indicator {\n"
"    border: 2px solid rgb(53, 53, 65);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(26, 26, 46);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid rgb(53, 53, 65);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBox_user.setObjectName("checkBox_user")
        self.btn_connect = QtWidgets.QPushButton(self.frame_login)
        self.btn_connect.setGeometry(QtCore.QRect(30, 333, 191, 41))
        self.btn_connect.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(26, 26, 46);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(26, 26, 46);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(100, 100, 100);\n"
"    background-color: rgb(15, 52, 96);\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    background-color: rgb(15, 52, 96);\n"
"    color: rgb(100, 100, 100);\n"
"}")
        self.btn_connect.setObjectName("btn_connect")
        self.horizontalLayout.addWidget(self.frame_login)
        self.verticalLayout.addWidget(self.frame_content)
        self.buttom_bar = QtWidgets.QFrame(self.centralwidget)
        self.buttom_bar.setMinimumSize(QtCore.QSize(0, 25))
        self.buttom_bar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.buttom_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttom_bar.setStyleSheet("background-color: rgb(15, 52, 96);")
        self.buttom_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttom_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttom_bar.setObjectName("buttom_bar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.buttom_bar)
        self.horizontalLayout_4.setContentsMargins(0, 0, 15, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_credit = QtWidgets.QLabel(self.buttom_bar)
        self.label_credit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_credit.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_credit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_credit.setObjectName("label_credit")
        self.horizontalLayout_4.addWidget(self.label_credit)
        self.verticalLayout.addWidget(self.buttom_bar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_error.setText(_translate("MainWindow", "Error"))
        self.btn_close_popup.setText(_translate("MainWindow", "X"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "USER"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.label_title.setText(_translate("MainWindow", "System Monitor"))
        self.checkBox_user.setText(_translate("MainWindow", "SAVE USER"))
        self.btn_connect.setText(_translate("MainWindow", "CONNECT"))
        self.label_credit.setText(_translate("MainWindow", "Created by: Oussama talaoui"))

import file_qrc

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Login()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

