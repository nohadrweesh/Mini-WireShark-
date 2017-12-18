# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packageDetails.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PacketDetails(object):
    def setupUi(self, PacketDetails):
        PacketDetails.setObjectName("PacketDetails")
        PacketDetails.resize(545, 497)
        self.centralwidget = QtWidgets.QWidget(PacketDetails)
        self.centralwidget.setObjectName("centralwidget")
        self.treeviewFarame = QtWidgets.QTreeView(self.centralwidget)
        self.treeviewFarame.setGeometry(QtCore.QRect(30, 30, 171, 31))
        self.treeviewFarame.setObjectName("treeviewFarame")
        self.treeviewEthernet = QtWidgets.QTreeView(self.centralwidget)
        self.treeviewEthernet.setGeometry(QtCore.QRect(30, 80, 171, 31))
        self.treeviewEthernet.setObjectName("treeviewEthernet")
        self.treeviewInternetProtocolVersion = QtWidgets.QTreeView(self.centralwidget)
        self.treeviewInternetProtocolVersion.setGeometry(QtCore.QRect(30, 130, 171, 31))
        self.treeviewInternetProtocolVersion.setObjectName("treeviewInternetProtocolVersion")
        self.treeviewTransmissionControlProtocol = QtWidgets.QTreeView(self.centralwidget)
        self.treeviewTransmissionControlProtocol.setGeometry(QtCore.QRect(30, 180, 171, 31))
        self.treeviewTransmissionControlProtocol.setObjectName("treeviewTransmissionControlProtocol")
        PacketDetails.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PacketDetails)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 21))
        self.menubar.setObjectName("menubar")
        PacketDetails.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PacketDetails)
        self.statusbar.setObjectName("statusbar")
        PacketDetails.setStatusBar(self.statusbar)

        self.retranslateUi(PacketDetails)
        QtCore.QMetaObject.connectSlotsByName(PacketDetails)

    def retranslateUi(self, PacketDetails):
        _translate = QtCore.QCoreApplication.translate
        PacketDetails.setWindowTitle(_translate("PacketDetails", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PacketDetails = QtWidgets.QMainWindow()
    ui = Ui_PacketDetails()
    ui.setupUi(PacketDetails)
    PacketDetails.show()
    sys.exit(app.exec_())

