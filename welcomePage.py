# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomePage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
interfaces=None
class Ui_WelcomeWireshark(object):
    def open_pckts_window(self,interface_chosen):
        #self.window = QtWidgets.QMainWindow()
        self.window = GuiForm(interface_chosen=interface_chosen)
        #self.ui.setupUi(self.window)
        WelcomeWireshark.hide()
        self.window.show()

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

        self.interfacesListView=QtWidgets.QListWidget(self.centralwidget)
        self.interfacesListView.setGeometry(QtCore.QRect(60, 160, 400, 400))
        self.make_custom_listview()
        self.interfacesListView.itemClicked.connect(self.item_chosen)


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

    def make_custom_listview(self):
        global  interfaces


        interfaces = get_interfaces_list()
        #interfaces=['noah','ali','fofo']
        for interface in interfaces:
           self.interfacesListView.addItem(interface["netid"])

    def item_chosen(self,item):
        # got to pckts lst with that item

        interface_num=self.interfacesListView.currentRow()
        interface_chosen=interfaces[interface_num]["name"]
        self.open_pckts_window(interface_chosen)

        print('you clicked ' + item.text()+"with number "+interface_chosen)
        #global  interface_chosen=i
from nerworkpro import  *



from welcomePageFunctions import *




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeWireshark = QtWidgets.QMainWindow()
    ui = Ui_WelcomeWireshark()
    ui.setupUi(WelcomeWireshark)
    WelcomeWireshark.show()
    sys.exit(app.exec_())

