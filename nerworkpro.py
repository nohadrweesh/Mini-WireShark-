# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nerworkpro.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
filter=''
from scapy.all import *
import datetime

pkts_sniffed =[]
num_of_packets=0

class GuiForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Wireshark()
        self.ui.setupUi(self)
        # self.tableView_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableView.itemClicked.connect(self.show_packet_details)
        self.ui.btnFilter.clicked.connect(self.filter_captured_packets)

        # self.show_packets_data()
        self.start_sniffing()

        

    def show_packets_data(self, item):
        global pkts_sniffed, num_of_packets
        rowPosition = self.ui.tableView.rowCount()
        self.ui.tableView.insertRow(rowPosition)
        pkts_sniffed.append(item)
        print(pkts_sniffed)
        self.ui.tableView.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(num_of_packets)))
        self.ui.tableView.setItem(rowPosition, 1,
                               QtWidgets.QTableWidgetItem(str((item.time))))
        self.ui.tableView.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(item[1].src))
        self.ui.tableView.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(item[1].dst))
        protocol=item[1].get_field('proto')
        field=protocol.i2s[item[1].proto]
        self.ui.tableView.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(field))
        self.ui.tableView.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(item[1].len)))
        self.ui.tableView.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem('info'))
        num_of_packets += 1

        # for m, item in enumerate(pkts_sniffed):
        #     self.ui.tableView.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(m+1)))
        #     self.ui.tableView.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(datetime.datetime.fromtimestamp(item.time))))
        #     self.ui.tableView.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(item[1].src))
        #     self.ui.tableView.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(item[1].dst))
        #     self.ui.tableView.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(item[1].proto)))
        #     self.ui.tableView.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(item[1].len)))
        #     self.ui.tableView.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem('info'))
        #     # self.ui.tableView.insertRow(rowPosition)
        #     rowPosition = self.ui.tableView.rowCount()
        #     self.ui.tableView.insertRow(rowPosition)

        self.ui.tableView.show()

    def show_packet_details(self, pcket_clicked):

        self.ui.hex_view.setText(hexdump(pkts_sniffed[pcket_clicked.row()], dump=True))
        self.ui.tableView_2.clear()

        pcket_details = parse_packet(str(pkts_sniffed[pcket_clicked.row()].show(dump=True)))
        print(pcket_details)

        for dic_key, detail_list in pcket_details.items():

            parent_node = QtWidgets.QTreeWidgetItem(self.ui.tableView_2)
            parent_node.setText(0, dic_key)
            for detail_index, detail in enumerate(detail_list):
                items = QtWidgets.QTreeWidgetItem(parent_node)
                items.setText(0, detail)

    def start_sniffing(self, interface=conf.iface, filter=''):
        sniff(count=10, iface=interface, filter=filter, prn=self.show_packets_data)
    #def callbackSetText(self, data):
        # Receiving data from sniffer thread
        # and puting them in a textedit widget
        #elf.ui.textedit.setText(data)

class Ui_Wireshark(object):
    def setupUi(self, Wireshark):
        Wireshark.setObjectName("Wireshark")
        Wireshark.resize(1260, 693)
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
        self.lineEdit.setGeometry(QtCore.QRect(80, 50, 1100, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.btnFilter=QtWidgets.QPushButton(self.centralwidget)
        self.btnFilter.setGeometry(QtCore.QRect(1110, 50, 50, 20))
        self.btnFilter.setObjectName("btnFilter")

        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(60, 110, 1200, 321))
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTreeWidget(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(60, 450, 561, 151))
        self.tableView_2.setObjectName("tableView_2")
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        #show pckets in table
        self.table_headers=['No','time','source','destination','protocol','length','info']




        #hex view

        self.hex_view = QtWidgets.QTextBrowser(self.centralwidget)
        self.hex_view.setGeometry(QtCore.QRect(700, 450, 561, 151))
        self.hex_view.setObjectName("hex_view_label")
        self.hex_view.setText("here is hex vals")


        self.tableView.setColumnCount(7)
        #self.tableView_2.setColumnCount(1)
        self.tableView.setHorizontalHeaderLabels(self.table_headers)



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






def analyze_packet(s):
    dict_pckets={}
    y=s.split("|<")

    y[0]=y[0].split('<')[-1]
    y[-1]=y[-1].split('|>')[0]
    y=y[:-1]
    for x in y:
        dict_pckets[x.split()[0]]=x.split()[1:]
    return dict_pckets

def parse_packet(d):

    ret_lst={}
    e= d.split("###[")[1:]
    for el in e:
        x=el.split("]###")
        #ret_lst[x[0]]=x[1]
        p=x[1].split("\n")[1:]

        ret_lst[x[0]] = p
    return ret_lst


from  Sniffer import  *
from PyQt5.QtCore import QObject, pyqtSignal

if __name__ == "__main__":
    # sniffer = Sniffer()
    # sniffer.start()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wireshark = GuiForm()
    # ui = Ui_Wireshark()
    # ui.setupUi(Wireshark)
    #Wireshark.connect(Wireshark, QtCore.SIGNAL('packetReceived(PyQt_PyObject)'),Wireshark. )

    Wireshark.show()

    sys.exit(app.exec_())

