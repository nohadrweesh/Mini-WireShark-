# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomePage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WelcomeWireshark(object):
    def setupUi(self, WelcomeWireshark):
        WelcomeWireshark.setObjectName("WelcomeWireshark")
        WelcomeWireshark.resize(482, 505)
        self.centralwidget = QtWidgets.QWidget(WelcomeWireshark)
        self.centralwidget.setObjectName("centralwidget")
        self.labelWelcome = QtWidgets.QLabel(self.centralwidget)
        self.labelWelcome.setGeometry(QtCore.QRect(50, 30, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelWelcome.setFont(font)
        self.labelWelcome.setObjectName("labelWelcome")
        self.LabelCapture = QtWidgets.QLabel(self.centralwidget)
        self.LabelCapture.setGeometry(QtCore.QRect(60, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelCapture.setFont(font)
        self.LabelCapture.setObjectName("LabelCapture")
        self.lineEditFiltering = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFiltering.setGeometry(QtCore.QRect(120, 100, 311, 21))
        self.lineEditFiltering.setObjectName("lineEditFiltering")
        self.LabelUingFilter = QtWidgets.QLabel(self.centralwidget)
        self.LabelUingFilter.setGeometry(QtCore.QRect(60, 120, 121, 16))
        self.LabelUingFilter.setObjectName("LabelUingFilter")
        WelcomeWireshark.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WelcomeWireshark)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 21))
        self.menubar.setObjectName("menubar")
        WelcomeWireshark.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WelcomeWireshark)
        self.statusbar.setObjectName("statusbar")
        WelcomeWireshark.setStatusBar(self.statusbar)

        self.retranslateUi(WelcomeWireshark)
        QtCore.QMetaObject.connectSlotsByName(WelcomeWireshark)

    def retranslateUi(self, WelcomeWireshark):
        _translate = QtCore.QCoreApplication.translate
        WelcomeWireshark.setWindowTitle(_translate("WelcomeWireshark", "MainWindow"))
        self.labelWelcome.setText(_translate("WelcomeWireshark", "Welcone to Wireshark "))
        self.LabelCapture.setText(_translate("WelcomeWireshark", "Captuer"))
        self.LabelUingFilter.setText(_translate("WelcomeWireshark", "....using this filter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeWireshark = QtWidgets.QMainWindow()
    ui = Ui_WelcomeWireshark()
    ui.setupUi(WelcomeWireshark)
    WelcomeWireshark.show()
    sys.exit(app.exec_())

