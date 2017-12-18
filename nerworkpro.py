# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nerworkpro.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wireshark(object):
    def setupUi(self, Wireshark):
        Wireshark.setObjectName("Wireshark")
        Wireshark.resize(708, 693)
        self.centralwidget = QtWidgets.QWidget(Wireshark)
        self.centralwidget.setObjectName("centralwidget")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(20, 0, 51, 31))
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setGeometry(QtCore.QRect(80, 0, 51, 31))
        self.btnStop.setObjectName("btnStop")
        self.labelSource = QtWidgets.QLabel(self.centralwidget)
        self.labelSource.setGeometry(QtCore.QRect(210, 80, 47, 21))
        self.labelSource.setObjectName("labelSource")
        self.labelDestination = QtWidgets.QLabel(self.centralwidget)
        self.labelDestination.setGeometry(QtCore.QRect(280, 80, 71, 21))
        self.labelDestination.setObjectName("labelDestination")
        self.labelProtocol = QtWidgets.QLabel(self.centralwidget)
        self.labelProtocol.setGeometry(QtCore.QRect(380, 80, 47, 21))
        self.labelProtocol.setObjectName("labelProtocol")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 310, 47, 13))
        self.label_7.setObjectName("label_7")
        self.labelLength = QtWidgets.QLabel(self.centralwidget)
        self.labelLength.setGeometry(QtCore.QRect(460, 80, 47, 21))
        self.labelLength.setObjectName("labelLength")
        self.labelTime = QtWidgets.QLabel(self.centralwidget)
        self.labelTime.setGeometry(QtCore.QRect(150, 80, 21, 21))
        self.labelTime.setObjectName("labelTime")
        self.labelInfo = QtWidgets.QLabel(self.centralwidget)
        self.labelInfo.setGeometry(QtCore.QRect(560, 80, 47, 21))
        self.labelInfo.setObjectName("labelInfo")
        self.labelNo = QtWidgets.QLabel(self.centralwidget)
        self.labelNo.setGeometry(QtCore.QRect(100, 70, 31, 41))
        self.labelNo.setObjectName("labelNo")
        self.labelFilter = QtWidgets.QLabel(self.centralwidget)
        self.labelFilter.setGeometry(QtCore.QRect(30, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelFilter.setFont(font)
        self.labelFilter.setObjectName("labelFilter")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 50, 501, 16))
        self.lineEdit.setObjectName("lineEdit")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(60, 110, 561, 321))
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(60, 450, 561, 151))
        self.tableView_2.setObjectName("tableView_2")
        Wireshark.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Wireshark)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Wireshark.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Wireshark)
        self.statusbar.setObjectName("statusbar")
        Wireshark.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Wireshark)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Wireshark)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(Wireshark)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Wireshark)
        QtCore.QMetaObject.connectSlotsByName(Wireshark)

    def retranslateUi(self, Wireshark):
        _translate = QtCore.QCoreApplication.translate
        Wireshark.setWindowTitle(_translate("Wireshark", "MainWindow"))
        self.btnStart.setText(_translate("Wireshark", "btnStart"))
        self.btnStop.setText(_translate("Wireshark", "btnStop"))
        self.labelSource.setText(_translate("Wireshark", "Source"))
        self.labelDestination.setText(_translate("Wireshark", "Destination"))
        self.labelProtocol.setText(_translate("Wireshark", "Protocol"))
        self.label_7.setText(_translate("Wireshark", "I"))
        self.labelLength.setText(_translate("Wireshark", "Lenght"))
        self.labelTime.setText(_translate("Wireshark", "Time"))
        self.labelInfo.setText(_translate("Wireshark", "Info"))
        self.labelNo.setText(_translate("Wireshark", "No."))
        self.labelFilter.setText(_translate("Wireshark", "Filter"))
        self.menuFile.setTitle(_translate("Wireshark", "File"))
        self.actionOpen.setText(_translate("Wireshark", "Open"))
        self.actionSave.setText(_translate("Wireshark", "Save"))
        self.actionExit.setText(_translate("Wireshark", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wireshark = QtWidgets.QMainWindow()
    ui = Ui_Wireshark()
    ui.setupUi(Wireshark)
    Wireshark.show()
    sys.exit(app.exec_())

