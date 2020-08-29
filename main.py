################################################################################
##
## BY: OUSSAMA TAHIRIA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 2.0.0
##
################################################################################

import sys
import platform
import psutil
import threading
import GPUtil
import re
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

## ==> LOGIN SCREEN
from ui_login import Ui_Login

## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen

## GUI FILE
from ui_main import Ui_MainWindow

## IMPORT FUNCTIONS
from ui_functions import *

## ==> GLOBALS
counter = 0

# LOGIN SCREEN
class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # BT CLOSE POPUP
        self.ui.btn_close_popup.clicked.connect(lambda: self.ui.frame_error.hide())

        # HIDE ERROR
        self.ui.frame_error.hide()

        # BT LOGIN
        self.ui.btn_connect.clicked.connect(self.checkFields)
        
        ## SHOW ==> LOGIN WINDOW
        ########################################################################
        self.show()

    #
    # FUNCTIONS
    #
    def checkFields(self):
        textUser = ""
        textPassword = ""

        def showMessage(message):
            self.ui.frame_error.show()
            self.ui.label_error.setText(message)

        # CHECK USER
        if not self.ui.lineEdit_user.text():
            textUser = " User Empyt. "
            #self.ui.lineEdit_user.setStyleSheet(self.ui.styleLineEditError)
        else:
            textUser = ""
            #self.ui.lineEdit_user.setStyleSheet(self.ui.styleLineEditOk)

        # CHECK PASSWORD
        if not self.ui.lineEdit_password.text():
            textPassword = " Password Empyt. "
            #self.ui.lineEdit_password.setStyleSheet(self.ui.styleLineEditError)
        else:
            textPassword = ""
            #self.ui.lineEdit_password.setStyleSheet(self.ui.styleLineEditOk)


        # CHECK FIELDS
        if textUser + textPassword != '':
            text = textUser + textPassword
            showMessage(text)
            #self.ui.frame_error.setStyleSheet(self.ui.stylePopupError)
        else:
            text = " Login OK. "
            if self.ui.checkBox_user.isChecked():
                text = text + " | Saver user: OK "
            showMessage(text)
            #self.ui.frame_error.setStyleSheet(self.ui.stylePopupOk)

            # SHOW SPLASH WINDOW
            self.main = SplashScreen()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("Zinus Corp.")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_loading.setText("Loading Database"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_loading.setText("Loading user interface"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.systemInformation)

        # TIMER IN MILLISECONDS
        self.timer.start(1000)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    ## SYSTEM INFORMATION
    def systemInformation(self):
        text = str(psutil.sensors_temperatures()['coretemp'][0])
        m = re.findall(r"\W current\D*(\d+.\d)", text)
        self.ui.label_22.setText(str(psutil.virtual_memory().percent) + "%")
        self.ui.label_18.setText(str(psutil.cpu_percent()) + "%")
        self.ui.label_20.setText("Temp: " + str(m[0]) + "C°")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())